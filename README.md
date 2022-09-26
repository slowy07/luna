# luna
text to image generation with stable diffusion

# output

```python
img = generator.generate(
  "DSLR photograph of an astronut ridinga horse",
  num_steps = 50,
  unconditional_guidance_scale = 75,
  temperature = 1,
  batch_size = 1,
)
```
output:

![astronut_horse](.github/result_output/astronaut_horse.png)

