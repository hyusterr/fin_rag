for agg_type in strict naive loose complex harsh
do
for early_stop_metric in valid_f1 valid_loss valid_disorder
do
if [ $early_stop_metric = "valid_f1" ]; then
    greater_is_better="True"
else
    greater_is_better="False"
fi
python3 train_highlighter.py \
    --output_dir ./checkpoints/$agg_type \
    --run_name $agg_type \
    --model_name bert-base-uncased \
    --train_agg_types $agg_type \
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better \
done
done

for agg_type in strict naive loose
do
for second_agg_type in strict naive loose
do
if [ $agg_type = $second_agg_type ]; then
    continue
fi
for early_stop_metric in valid_f1 valid_loss valid_disorder
do
if [ $early_stop_metric = "valid_f1" ]; then
    greater_is_better="True"
else
    greater_is_better="False"
fi
# iterative training
python3 train_highlighter.py \
    --output_dir ./checkpoints/iterate_$agg_type-$second_agg_type \
    --run_name iterate_$agg_type-$second_agg_type \
    --model_name bert-base-uncased \
    --train_agg_types $agg_type
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better \

python3 train_highlighter.py \
    --output_dir ./checkpoints/iterate_$agg_type-$second_agg_type \
    --run_name iterate_$agg_type-$second_agg_type \
    --model_name bert-base-uncased \
    --train_agg_types $second_agg_type \
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better \
    --resume_from_checkpoint True \

# curriculum training
python3 train_highlighter.py \
    --output_dir ./checkpoints/curriculum_$agg_type-$second_agg_type \
    --run_name curriculum_$agg_type-$second_agg_type \
    --model_name agg_highlighter \
    --train_agg_types $agg_type $second_agg_type \
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better \
    --agg_strategy curriculum \
    --agg_type_order $agg_type $second_agg_type 

# mix training
python3 train_highlighter.py \
    --output_dir ./checkpoints/mix_$agg_type-$second_agg_type \
    --run_name mix_$agg_type-$second_agg_type \
    --model_name agg_highlighter \
    --train_agg_types $agg_type $second_agg_type \
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better \
    --agg_type_weights 0.5 \
    --agg_strategy mix \
    --agg_type_order $agg_type $second_agg_type

done
done
done

# no train
# cnc_highlighter
python3 train_highlighter.py \
    --output_dir ./checkpoints/cnc_highlighter \
    --run_name cnc_highlighter_inference \
    --model_name cnc_highlighter \
    --train_model False 

python3 train_highlighter.py \
    --output_dir ./checkpoints/bert-base-untrain \
    --run_name bert_inference \
    --model_name bert-base-uncased \
    --train_model False 

# train cnc_highlighter
for agg_type in strict naive loose complex harsh
do
for early_stop_metric in valid_f1 valid_loss valid_disorder
do
if [ $early_stop_metric = "valid_f1" ]; then
    greater_is_better="True"
else
    greater_is_better="False"
fi
python3 train_highlighter.py \
    --output_dir ./checkpoints/cnc_$agg_type \
    --run_name cnc_$agg_type \
    --model_name cnc_highlighter \
    --train_agg_types $agg_type \
    --metrics_for_best_model $early_stop_metric \
    --greater_is_better $greater_is_better 
done
done
