# we still use is_newsroom=true to handle our own preprocessed input
python run_summarization.py --mode=train --data_path=./data/cnndm_train.tsv --vocab_path=./data/cnndm.vocab --log_root=./log --exp_name=cnndm --is_newsroom=true --max_steps=230000
