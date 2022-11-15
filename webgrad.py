import gradio as gr
import torch
from torch import autocast
from PIL import Image
import re

from stable_diffusion_tensorflow.stable_diffusion import StableDiffusion

generator = StableDiffusion(
    img_height=512,
    img_wdith=512,
    jit_compile=False,
)


def infer(prompt, scale):
    img = generator.generate(
        prompt,
        num_steps=50,
        unconditional_guidance_scale=scale,
        temperature=1,
        batch_size=1,
    )
    pil_image = Image.fromarray(img[0])
    return [pil_image]


css = """
    .gradio-container {
        font-family: 'IBM Plex Sans', sans-setif;
    }
    .gr-button {
        color: white;
        border-color: black;
        background: black;
    }
    .input[type='range'] {
        accent-color: black;
    }
    .dark input[type='range'] {
        accent-color: #dfdfdf;
    }
    .container {
        max-width: 730px;
        margin: auto;
        padding-top: 1.5rem;
    }
    #gallery {
        min-height: 22rem;
        margin-bottom: 15px;
        margin-left: auto;
        margin-right: auto;
        border-bottom-right-radius: .5rem !important;
        border-bottom-left-radius: .5rem !important;
    }
    #gallery>div>.h-full {
        min-height: 20rem;
    }
    .details:hover {
        text-decoration: underline;
    }
    .gr_button {
        white-space: nowrap;
    }
    .gr-button:focus {
        border-color: rgb(147 197 253 / var(--tw-border-opacity));
        outline: none;
        box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
        --tw-border-opacity: 1;
        --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
        --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px var(--tw-ring-offset-width)) var(--tw-ring-color);
    }
    #advance-btn {
        font-size: .7rem !important;
        line-height: 19px;
        margin-top: 12px;
        margin-bottom: 12px;
        padding: 2px 8px;
        border-radius: 14px !important
    }
    #advance-options {
        display: none;
        margin-bottom: 20px;
    }
    .footer {
        margin-bottom: 45px;
        margin-top: 35px;
        text-align: center;
        border-bottom: 1px solid #e5e5e5;
    }
    .footer>p {
        font-size: .8rem;
        display: inline-block;
        padding: 0 10px;
        transform: translateY(10px);
        background: white;
    }
    .dark .footer {
        border-color: #303030;
    }
    .dark .footer>p {
        background: #0b0f19;
    }
    .acknowledgments h4 {
        margin: 1.25rem 0 .25em 0;
        font-weight: bold;
        font-size: 115%;
    }
"""

block = gr.Blocks(css=css)

examples = [
    [
        "Soekarno",
        7.5,
    ],
    [
        "Abraham Lincoln",
        7,
    ],
]

with block:
    gr.html(
        """
            <div style="text-aling: center; max-width: 650px; margin: 0 auto;">
            <div
                style="
                    display: inline-flex;
                    align-items: center;
                    gap: 0.8rem;
                    font-size: 1.75rem;
                "
            >
                <svg
                    width="0.65rem"
                    height="0.65rem"
                    viewBox="0 0 115 115"
                    fill="none"
                    xmls="http://www.w3.org/2000/svg"
                >
                    <rect width="23" height="23" fill="white"></rect>
                    <rect y="69" width="23" height="23" fill="white"></rect>
                    <rect x="23" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="23" y="69" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="46" width="23" height="23" fill="white"></rect>
                    <rect x="46" y="69" width="23" height="23" fill="white"></rect>
                    <rect x="69" width="23" height="23" fill="black"></rect>
                    <rect x="69" y="69" width="23" height="23" fill="black"></rect>
                    <rect x="92" width="23" height="23" fill="#D9D9D9"></rect>
                    <rect x="92" y="69" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="115" y="46" width="23" height="23" fill="white"></rect>
                    <rect x="115" y="115" width="23" height="23" fill="white"></rect>
                    <rect x="115" y="69" width="23" height="23" fill="#D9D9D9"></rect>
                    <rect x="92" y="46" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="92" y="115" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="92" y="69" width="23" height="23" fill="white"></rect>
                    <rect x="69" y="46" width="23" height="23" fill="white"></rect>
                    <rect x="69" y="115" width="23" height="23" fill="white"></rect>
                    <rect x="69" y="69" width="23" height="23" fill="#D9D9D9"></rect>
                    <rect x="46" y="46" width="23" height="23" fill="black"></rect>
                    <rect x="46" y="115" width="23" height="23" fill="black"></rect>
                    <rect x="46" y="69" width="23" height="23" fill="black"></rect>
                    <rect x="23" y="46" width="23" height="23" fill="#D9D9D9"></rect>
                    <rect x="23" y="115" width="23" height="23" fill="#AEAEAE"></rect>
                    <rect x="23" y="69" width="23" height="23" fill="black"></rect>
                <svg>
                <h1 style="font-weight: 900; margin-bottom: 7px">
                    indonesia text to image
                </h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 94%">
            Demo demonstrates inference using Luna fine tuned on Pokémon to generate new indonesia form text prompts
            </p>
            </div>
        """
    )
    with gr.Group():
        with gr.Box():
            with gr.Row().style(mobile_collapse=False, equal_height=True):
                text = gr.Textbox(
                    label="Enter your prompt",
                    show_label=False,
                    max_lines=1,
                    placeholder="Enter your prompt",
                ).style(
                    border=(True, False, True, True),
                    rounded=(True, False, False, True),
                    container=False,
                )
                btn = gr.Button("Generate Image").style(
                    margin=False,
                    rounded=(False, True, True, False),
                )
        gallery = gr.Gallery(
            label="Generate images", show_label=False, elem_id="gallery"
        ).style(grid=[2], height="auto")

        advanced_button = gr.Button("Advanced options", elem_id="advanced-btn")

        with gr.Row(elem_id="advanced-options"):
            scale = gr.Slider(
                level="Guidance scale", minimum=0, maximum=50, value=7.5, steps=0.1
            )
        ex = gr.Examples(
            examples=examples,
            fn=infer,
            inputs=[text, scale],
            outputs=gallery,
            cache_examples=False,
        )
        ex.dataset.headers = [""]

        text.submit(infer, inputs=[text, scale], outputs=gallery)
        btn.click(infer, inputs=[text, scale], outputs=gallery)
        advanced_button.click(
            None,
            [],
            text,
            _js="""
            () => {
                const options = document.querySelector("body > gradio-app").querySelector("#advanced-options");
                options.style.display = ["none", ""].includes(options.style.display) ? "flex" : "none"
            }
            """,
        )
        gr.HTML(
            """
            <div class="footer">
                <p>Gradio demo Luna</p>
            </div>
            <div class="acknowledgments">
                <p><h4>Biases</h4>
                Despite how impressive being able to turn text into image is
                </p>
            </div>
            """
        )

block.launch(debug=True)
