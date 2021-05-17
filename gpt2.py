from sklearn.model_selection import train_test_split
import pickle

data = pickle.load(open("/content/drive/MyDrive/tweets_afd.p", "rb"))

def build_txt(data, path):
  with open(path, "w") as f:
    f.writelines(data)



train, test = train_test_split(data,test_size=0.15)

build_txt(train,'train_dataset.txt')
build_txt(test,'test_dataset.txt')

#print("Train dataset length: "+str(len(train)))
#print("Test dataset length: "+ str(len(test)))



! pip install git+git://github.com/huggingface/transformers/
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("anonymous-german-nlp/german-gpt2")

train_path = 'train_dataset.txt'
test_path = 'test_dataset.txt'

from transformers import TextDataset,DataCollatorForLanguageModeling

def load_dataset(train_path,test_path,tokenizer):
    train_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path=train_path,
          block_size=128)

    test_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path=test_path,
          block_size=128)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
    return train_dataset,test_dataset,data_collator

train_dataset,test_dataset,data_collator = load_dataset(train_path,test_path,tokenizer)

from transformers import Trainer, TrainingArguments, AutoModelWithLMHead

model = AutoModelWithLMHead.from_pretrained("anonymous-german-nlp/german-gpt2")

training_args = TrainingArguments(
    output_dir="./gpt2-afd", #The output directory
    overwrite_output_dir=True, #overwrite the content of the output directory
    num_train_epochs=6, # number of training epochs
    per_device_train_batch_size=32, # batch size for training
    per_device_eval_batch_size=64,  # batch size for evaluation
    eval_steps=400, # Number of update steps between two evaluations.
    save_steps=800, # after # steps model is saved
    warmup_steps=500,# number of warmup steps for learning rate scheduler
    )

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    # prediction_loss_only=True,
)

trainer.train("/content/gpt2-afd/checkpoint-4800")

trainer.save_model()

from transformers import pipeline

afd = pipeline('text-generation',model='/content/drive/MyDrive/afd_model', tokenizer='anonymous-german-nlp/german-gpt2',config={'max_length':2000})


for i in range(10):
  result = afd('Zuwanderung')[0]['generated_text']
  print(result)
  print()
