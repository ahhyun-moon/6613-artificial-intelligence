# Milestone 3-4: 
## Milestone 3: Finetuning Language Models (Week 5, 40 points)
### Link to Huggingface Space: 

[https://huggingface.co/spaces/moonahhyun/project-uspto](https://huggingface.co/spaces/moonahhyun/project-uspto)

### Link to Finetuned Model: 

[https://huggingface.co/moonahhyun/project-uspto](https://huggingface.co/moonahhyun/project-uspto)

### Link to Colab (training):

[https://colab.research.google.com/drive/1wX9z8oSRJDCJi-le1arXqSujDSisZ3kU?usp=sharing](https://colab.research.google.com/drive/1wX9z8oSRJDCJi-le1arXqSujDSisZ3kU?usp=sharing)

## Milestone 4: Documentation and Video Production (Week 6, 20 points)
### Link to App Landing Page: 

[https://sites.google.com/nyu.edu/cs-gy-6613-project/home](https://sites.google.com/nyu.edu/cs-gy-6613-project/home)

**The above Google Site includes:**
- Links to current Github page, Huggingface Space, and Google Colab notebook
- App demonstration video
- Embedded Patentability Score App 

<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/milestone-3-4/project/milestone-3-4/0.google_site.png" width=800/>

### Link to Video: 

[https://youtu.be/ULQ8bn5XNMQ](https://youtu.be/ULQ8bn5XNMQ)

# Finetuned Model (Result)

The model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on HUPD dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4697
- Accuracy: 0.8003

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4911        | 1.0   | 545  | 0.4736          | 0.7964   |
| 0.4744        | 2.0   | 1090 | 0.4697          | 0.8003   |


### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.0+cu118
- Datasets 2.11.0
- Tokenizers 0.13.3



