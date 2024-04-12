## Why
Why twist and torture your brain like this? Because it's [fun and educational](https://twitter.com/karpathy/status/1778153659106533806). 

## Context
Found professor Rush's repo, [srush/Tensor-Puzzles](https://github.com/srush/Tensor-Puzzles). It's useful because working with transformer has to deal with padding, attention mask, collate function and packing. Getting used to thinking in tensor helps. 

I prefer mastering few universal primitives over memorizing many APIs, ex: `einsum`, `einops`. The hope is better readability and less bug by reducing the contact surface and keep things simple. The goal is learning fundamentals with practices of reducing high level tensor ops to core primitives. 

Made few changes wrt [srush/Tensor-Puzzles](https://github.com/srush/Tensor-Puzzles) to better fit my preference:
- Explicit example: easier to understand expected IO spec.
- Explicit test case: easier to debug. 
- Backend to numpy: doesn't matter since all reduce to basic ops. numpy, pytorch, jax, mlx all work the same. 
- Change signature of few ops. 
- [Shape suffix style](https://medium.com/@NoamShazeer/shape-suffixes-good-coding-style-f836e72e24fd): ex: `a_i` is an 1 dimension tensor `a` with the size `i`. 

> Warning: be careful in production. One bad night sleep, colon, comma, index off by one, wrong dimension inserted or wrong direction of >, the code is messed up and you would spend days to find that bug. What's worse is that training may still work. These small hidden logic bombs would be chipping performance away in the shadow. 


## How to?
Install dependency: 
```bash
pip install numpy
```

Work on `puzzle.ipynb` on your own. Use `solution_and_note.ipynb` as reference. I use `numpy` native api for example so no dependency on custom functions. Uncomment the sanity check and test cell to try your implementation. 

What works really well for me is to set a limit, say 10 mins. If I can't figure out in 10m, mark the puzzle, move on to the next one. Usually the problem would be resolved after a walk or shower. If super blocked, quick peak at the reference and try again. Don't be frustrated. Stay calm, try harder, try again, repeat. 

Apply [spaced repetition](https://gwern.net/spaced-repetition). After few rounds in few days, you would get used to those twisted, super weird patterns, and approach tensor manipulation with new perspectives for your future [yolo runs](https://twitter.com/_jasonwei/status/1757486124082303073).  


## Reference
- All credit to [srush/Tensor-Puzzles](https://github.com/srush/Tensor-Puzzles). He has created many educational repos. Go check it out! 
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) explained in numpy doc. 
- Sasha's poem on broadcasting is succinct. ![](https://camo.githubusercontent.com/75af16f9099f8473e04eedb662376447802133951618c181d20023f443197b8e/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f465179776f723057594173736e37593f666f726d61743d706e67266e616d653d6c61726765)