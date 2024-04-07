# tensor_puzzle
## Context
- Padding, attention mask, collate function and packing. 
- I'm bad at memorizing and retrieving from lots of api signatures. Prefer to minimize the contact surface, ex: einsum, einops. Function calling could be done better by LLM. 
- Visual example and color coding is killing me. Direct example would be fine, since this is 1 or 2d only. 
- Since I don't know the api, the name of the puzzle mean nothing to me. Clear input output example is very important, not color coding. Spec is too cumbersome to read to understand the shape and rearrangement. 
- Test failure message is cryptic. 

## What is this for? 
- Pure brain gymnastics. The purpose is expanding the understanding of tensor manipulation.

## Warning
- Production code in this style would be too coder mental state dependent. The style is destined to be the source of deadly bugs. The readability is close to 0. 
- One could go crazy and intensive during practice, but it's better to stay simple and effective in production. 
- Insisting on coding in first principle on all circumstances is more about ego than skill, borderline stupid.
- Bad night sleep, one colon, comma, index off by one, wrong dimension squeezed or wrong direction of >, the code is messed up and you would spend days to find that bug.
- What's worse, the training still works, no loss spike and keep improving. Silent logic bombs scattering all over the code base to kill the performance in the shadow.
- The pros of using built in API is stable, clear, atomic interface based on tested, even optimized implementation.
- "But Claude Opus or gpt(n+1) could operate on this level with no bugs!" Now we are back to superalignment 101, if the output is 1k line of code, how can you be sure ...?

## How to use this?
- Suggest you work on one puzzle for 5 mins, if still blank, quick peek at the solution and try again. Still blank, read the solution and notes and try again. Still blank, type in the solution, mark the question for review, move on. Don't fret over it. Replay and repetition is the cure for out of distribution task, that's all. 
- Rinse and repeat few time in few days. Give your brain enough time and triggers to rewire and learn deeper representations, aka spaced interval learning. 


## TODO
- [ ] Make this an eval set for testing LLM or agent. 