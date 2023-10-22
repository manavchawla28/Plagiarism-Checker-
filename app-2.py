import gradio  as gr
from redlines import Redlines


def test(input1, input2): 
    
    diff=Redlines(input1,input2)

    otp= diff.output_markdown

    return "<br>"+ "<br>""<br>"+otp+"<br>"+ "<br>"+"<br>"+ "<br>"


with gr.Blocks() as demo:

    gr.Markdown("""# Text Compare -Redline and Strikethrough""")
    gr.Markdown(""" Enter first and second text and hit Start Comparrison button""")
    gr.Markdown(""" """)
    

    with gr.Row(scale=1):
        input1 = gr.Textbox(label="Enter first text ")
        input2     = gr.Textbox(label="Enter second text")    
    run_btn     = gr.Button("Start comparrison")    
    otp = gr.outputs.HTML(label="Redline & Strikethrough")
    run_btn.click(fn=test, inputs=[input1, input2], outputs=[otp])


demo.launch(debug=True)