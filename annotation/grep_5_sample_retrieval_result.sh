for target_id in $(cat $1); do
    company_id=$(echo $target_id | cut -d'_' -f3)
    year=2022
    dir_name=${company_id}_${year}
    for system in w_mda wo_mda retrieval_results.txt; do
        grep ${target_id}' ' retrieval_results/$dir_name/$system >> retrieval_results/5_sample/$system
    done
    cat retrieval_results/5_sample/* > retrieval_results/5_sample/merged.txt
done
