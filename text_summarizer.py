from transformers import pipeline
import image_to_text     # if this program are exucutes in main thread.


# it generates text summary by using transformers, helps to convert large text into one paragraph.
def get_summary(text):
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")
    summary = summarizer(text, max_length=15, min_length=5, do_sample=False)
    return summary[0]['summary_text']


if __name__ == "__main__":
    img_path = "Images/A Sofa.png"
    input_text = image_to_text.extract_text_from_image(img_path)
    summary = get_summary(input_text)
    print(summary)