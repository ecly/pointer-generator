# We still use is_newsroom=true to handle our own preprocessed input

# Train for the initial 230_000 iterations without coverage
# python run_summarization.py --mode=train --data_path=./data/cnndm_train.tsv --vocab_path=./data/cnndm.vocab --log_root=./log --exp_name=cnndm --is_newsroom=true --max_steps=230000

# Convert the model to a coverage version
# python run_summarization.py --mode=train --data_path=./data/cnndm_train.tsv --vocab_path=./data/cnndm.vocab --log_root=./log --exp_name=cnndm --is_newsroom=true --max_steps=233000 --convert_to_coverage=True --coverage=True

# Train the coverage enabled model for 3000 iterations
python run_summarization.py --mode=train --data_path=./data/cnndm_train.tsv --vocab_path=./data/cnndm.vocab --log_root=./log --exp_name=cnndm --is_newsroom=true --max_steps=233000 --coverage=True
