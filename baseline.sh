for retr in all-mpnet dpr hybrid multi_fields; do
    for hl in cnc; do
        for lt in 0.5; do
            echo "Retriever: ${retr} + Highlighter: ${hl}"
            python3 task1_eval.py -tf annotation/annotated_result/all/aggregate_qlabels.jsonl -rf result/all/${retr}.trec -hl ${hl} -lt ${lt} -d cuda:1 | tee result/all/R.${retr}_H.${hl}.result
        done
    done
done
