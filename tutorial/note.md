# transformers
## tokenizer
example: 
```python
# text = 'today is not that bad'
from transformers import AutoTokenizer
1. tokens = AutoTokenizer.tokenize(text)
2. input_ids = AutoTokenizer.convert_tokens_to_ids(tokens)
3. input_ids = AutoTokenizer.built_inputs_with_special_tokens(input_ids)
4. AutoTokenizer.encode(text) = AutoTokenizer.built_inputs_with_special_tokens(AutoTokenizer.convert_tokens_to_ids(AutoTokenizer.tokenize(text)))
5. AutoTokenizer.decode(input_ids)
```
Attention:
1. 单句输入 -> input_ids
2. 多句输入 -> attention_mask
3. 两句拼接 -> token_type_ids
4. tokenizer 不会轻易地把一个词处理为`[UNK](100)`
5. tokenize, encode, decode
    - tokenize: word -> token
    - encode: token -> id
    - decode: id -> token -> word
## model
1. model architecture
2. model learnable parameters
    ```python
    total_learnbale_params = 0
    for name, param in model.named_parameters():
        if param.requires_grad:
            total_learnable_params += param.numel()
    ```
3. torch.no_grad() vs. param.requires_grad = False
4. input embedding = token embedding + position embedding + segment embedding
```python
token_embedding = model.embeddings.word_embeddings(input_ids)
position_embedding = model.embeddings.position_embeddings(position_ids)
segment embedding = model.embeddings.token_type_embeddings(token_type_ids)
input_embedding = token_embedding + position_embedding + segment_embedding
input_embedding = model.embeddings.LayerNorm(input_embedding)
input_embedding = model.embeddings.droupout(input_embedding)
```
## output
- len(outputs) == 3
- outputs[0]
    - last_hidden_state, shape: batch_size * seq_len * hidden_size (1 * 22 * 768)
- outputs[1]
    - pooler_output, shape: batch_size * hidden_size (1 * 768)
    - Last layer hidden-state of the first token of the sequence(classification token, [cls])
- outputs[2]`(model.config.output_hidden_states=True)`
    - hidden_states
    - type: tuple
    - one for the output of the embeddings, if the model has an embedding layer, + one for the output of each layer
    = (1 + 12)\*(batch_size\*seq_len\*hidden_size) = 13 *1 * 22 * 768
- outputs[0] = outputs[2][-1]
- outputs[1] = model.pooler(outputs[2][-1])
- outputs[2][0] = model.embeddings(token_inpus['input_ids'], token_inputs['token_type_ids'])