import json
import argparse
import pandas as pd


def prepare_annotation_template(filename):
    """
    filename: .jsonl filename
        first line: {"form": "10-Q", "filing_date": "20180426", "name": "Microsoft Corp", "cik": "789019"}
        other lines: {"id": "20180426_10-Q_789019_part1_item1_para133", "order": 133, "paragraph": ["19,792"], "table": [...]}
    
    desired output: a excel file for annotation usage
    - filename: info from the first line
    - row set <--> 1 line in the original file:
        - original text (for readabliity)
        - tokens (for annotation): 1 cell 1 token
        - labels (for annotation): 1 cell 1 label (0/1)
    """
    output = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    info = json.loads(lines[0])
    output.append([lines[0].strip()])
    output.append(['label explanation'])
    output.append(['0', 'not target'])
    output.append(['1', 'Company-specific knowledge'])
    output.append(['2', 'Change/Action related to financial entities in the given period'])
    output.append(['3', 'The reason of changes in this period'])
    output.append(['4', 'Mention of other documents'])
    output.append(['5', 'Others'])
    output.append([''])


    for i in range(1, len(lines)):
        line = json.loads(lines[i])
        id_ = line['id']
        item = id_.split('_')[-2]
        if item != 'item7':
            continue
        order = line['order']
        paragraph = line['paragraph'][0]
        tokens = paragraph.split(' ')
        labels = [0] * len(tokens)
        output.append([id_, paragraph])
        output.append(['tokens'] + tokens)
        output.append(['label'] + labels)
        output.append([''] * len(tokens))

    df = pd.DataFrame(output)
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default='targets/20201030_10-K_320193.jsonl')
    parser.add_argument('--output', type=str, default='test.xlsx')
    args = parser.parse_args()

    df = prepare_annotation_template(args.filename)
    df.to_excel(args.output, index=False, header=False)
    print(f'Annotation template saved to {args.output}')
