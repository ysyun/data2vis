export DATA_DIR=.
python -m bin.train \
  --config_paths="
      $DATA_DIR/example_configs/nmt_$1.yml,
      $DATA_DIR/example_configs/train_seq2seq.yml,
      $DATA_DIR/example_configs/text_metrics_bpe.yml" \
  --model_params "
      vocab_source: $DATA_DIR/sourcedata/vocab.source
      vocab_target: $DATA_DIR/sourcedata/vocab.target" \
  --input_pipeline_train "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        - $DATA_DIR/mydata/sourcedata/train.sources
      target_files:
        - $DATA_DIR/mydata/sourcedata/train.targets" \
  --input_pipeline_dev "
    class: ParallelTextInputPipeline
    params:
       source_delimiter: ''
       target_delimiter: ''
       source_files:
        - $DATA_DIR/mydata/sourcedata/dev.sources
       target_files:
        - $DATA_DIR/mydata/sourcedata/dev.targets" \
  --batch_size 32 \
  --train_steps 1000 \
  --output_dir $DATA_DIR/mydata/vizmodel-$1
