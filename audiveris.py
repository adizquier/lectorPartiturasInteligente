import subprocess
from music21 import converter

def audiveris_aviable():
    try:
        subprocess.run(["flatpak", "run", "org.audiveris.audiveris", "-version"], capture_output=True)
        return True
    except (subprocess.CalledProcessError):
        return False

def convert_pdf_to_midi(pdf_file, midi_file, nombreArchivo):
    # Comando para convertir PDF a MIDI con Audiveris mediante Flatpak
    command = [
        "flatpak", "run", "org.audiveris.audiveris",
        "-batch", "-export", "-output", midi_file,"--", pdf_file
    ]

    try:
        # Ejecutar el comando
        subprocess.run(command, check=True)
        
        
        conv=converter.parse(midi_file+nombreArchivo+".mxl")
        midi = "./archivosMIDI/"+nombreArchivo+".midi"
        conv.write('midi', midi)

        return midi

    except subprocess.CalledProcessError as e:
        print(f"Error al convertir {pdf_file} a {midi_file}: {e}")

def convert_pages_to_midi(pagina, outputXML, outputMIDI, nombreArchivo):
    command = [
        "flatpak", "run", "org.audiveris.audiveris",
        "-batch", "-export", "-output", outputXML,"--", pagina
    ]

    try:
        # Ejecutar el comando
        subprocess.run(command, check=True, capture_output=True)
        
        conv=converter.parse(outputXML+nombreArchivo+".mxl")
        midi = outputMIDI + nombreArchivo + ".midi"
        conv.write('midi', midi)

        return midi

    except subprocess.CalledProcessError as e:
        print(f"Error al convertir {pagina} a {outputXML}: {e}")


