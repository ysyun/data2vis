python -m bin.infer \
  --tasks "
    - class: DecodeText
      params:
        delimiter: '' " \
  --model_dir vizmodel \
  --model_params "
    inference.beam_search.beam_width: 2" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        -  test.txt "
