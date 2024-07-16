import streamlit as st
import PyPDF2 

# BACK ---------------------

# VARIABLES --
output_pdf = "documents/pdf_final.pdf"

#FUNCIONES --
def unir_pdf(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()

    for docu in documents:
        pdf_final.append(docu)

    pdf_final.write(output_path)




# FRONT --------------------
st.image("/assets/pdf.png", width=250)
st.header("Unir PDFs")
st.subheader("Adjuntar PDF para unirlos")

pdf_adjuntos = st.file_uploader("Seleciona una imagen", accept_multiple_files=True)

unir = st.button("Unir PDFs")



if unir:
    if len(pdf_adjuntos) < 1:
        st.warning("Seleccione mas de un PDF para unir")
    else:
        unir_pdf(output_pdf, pdf_adjuntos)
        st.success("Desde aqui puede descar el PDF final")
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button("Descargar PDF final", data=pdf_data, file_name="pdf_final.pdf")
