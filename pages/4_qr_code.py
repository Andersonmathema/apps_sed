import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Título do app
st.title("Gerador de QR Code")

# Entrada de texto para o usuário
input_data = st.text_input("Insira o texto ou URL para gerar o QR Code:")

# Botão para gerar o QR Code
if st.button("Gerar QR Code"):
    if input_data:
        # Gerar o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)

        # Criar imagem do QR Code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Converter a imagem para bytes para exibir no Streamlit
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Exibir o QR Code no Streamlit
        st.image(byte_im, caption="QR Code Gerado", use_column_width=True)

        # Botão para baixar o QR Code
        st.download_button(
            label="Baixar QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png",
        )
    else:
        st.error("Por favor, insira um texto ou URL válido.")

