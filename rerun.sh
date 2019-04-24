# Train initial Pointer Generator model
python run_summarization.py --mode=train --data_path=data/chunked/train_* --vocab_path=data/vocab --log_root=log --exp_name=rerun --iterations 230000

# Evaluate Pointer Generator
python run_summarization.py --mode=decode --data_path=data/chunked/test_* --vocab_path=data/vocab --log_root=log --exp_name=rerun --single_pass=True

# Convert model to coverage
python run_summarization.py --log_root=log --exp_name=rerun --covert_to_coverage=True --coverage=True

# Convert model to coverage
python run_summarization.py --mode=train --log_root=log --exp_name=rerun --iterations 233000 --coverage=True

# Evaluate Pointer Generator + Coverage
python run_summarization.py --mode=decode --data_path=data/chunked/test_* --vocab_path=data/vocab --log_root=log --exp_name=rerun --single_pass=True --coverage=True
