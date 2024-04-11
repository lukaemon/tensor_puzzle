# tensor_puzzle
Found professor Rush's repo, [srush/Tensor-Puzzles](https://github.com/srush/Tensor-Puzzles). It's useful because working with transformer has to deal with padding, attention mask, collate function and packing. Getting used to thinking in tensor natively helps. 

I personally prefer mastering few fairly universal primitives over memorizing many APIs, ex: `einsum`, `einops`. The hope is better readability and less bug by reducing the contact surface and keep things simple. The goal is with practices that reduce common tensor op to few primitives, one would gain better understanding about `broadcasting`, `matmul`, `dot product` and `indexing`. 

Made few changes wrt [srush/Tensor-Puzzles](https://github.com/srush/Tensor-Puzzles) to better fit my preference:
- Explicit example: easier to understand expected IO spec.
- Explicit test case: easier to debug. 
- Backend to numpy: doesn't matter since all reduce to basic ops.
- Change signature of few ops. 
- [Shape suffix style](https://medium.com/@NoamShazeer/shape-suffixes-good-coding-style-f836e72e24fd): you will see something like `a_i` in the signature. It means an one dimension tensor `a`, the size of the dimension is `i`. 

> Warning: be careful in production. One bad night sleep, colon, comma, index off by one, wrong dimension inserted or wrong direction of >, the code is messed up and you would spend days to find that bug. What's worse is that training may still work. These small hidden logic bombs are eating performance in the shadow. Think about pros and cons between well tested, explicit api and primitives wrt production needs. 
