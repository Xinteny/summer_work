- Pipeline
将数据预处理、模型调用、结果后处理三部分组装成流水线，使我们能够直接输入文本就获得最终的答案 
[tokenizer|model|post processing]
- Model Head
连接在模型后的层，通常为1个或多个全连接层，将模型编码的表示结果进行映射，以解决不同类型的任务

