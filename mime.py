def get_mime_type(file):
        if is_pdf(file):
                return "application/pdf"
        elif is_zip(file):
                return "application/zip"
        elif is_xml(file):
                return "text/xml"
        elif is_html(file):
                return "text/html"
        elif is_plain(file):
                return "text/plain"
        elif is_png(file):
                return "image/png"
        elif is_jpeg(file):
                return "image/jpeg"
        elif is_gif(file):
                return "image/gif"
        else:
                return "unknown type"
 

 
 
def is_pdf(file):
        file = open(file, 'rb')
        bs = file.read(5)
        file.close()
        return bs == b'%PDF-'
 
 
def is_zip(file):
        file = open(file, 'rb')
        bs = file.read(4)
        file.close()
        return bs == b'PK\x03\x04'
 
 
 
def is_xml(file):
        file = open(file, 'rb')
        bs = file.read(5)
        file.close()
        return bs == b'<?xml'
 
 
def is_html(file):
        file = open(file, 'rb')
        bs = file.read(14)
        file.close()
        return bs == b'<!DOCTYPE html'
 
 
def is_plain(file):
        def is_punctuation_mark(ch):
                return ch in [
                        ',', '.', '/', ':', ';', '"', '?', '!'
                        , '(', ')', '\\', '>', '<', "'", '*', '%'
                        , '$', '@', '#', '^', '&', '~', '[', ']'
                        , '{', '}', '|', '-'
                ]
 
        file = open(file, 'rb')
        bs = file.read()
        bs = list(map(lambda x: chr(x), bs))
        for b in bs:
                if not (b.isalnum() or b.isspace() or is_punctuation_mark(b)):
                        return False
        return True
 
 
 
 
def is_png(file):
        file = open(file, 'rb')
        bs = file.read(11)
        file.close()
        return bs == b'\x89PNG\r\n\x1a\n\x00\x00\x00'
 
 
def is_jpeg(file):
        file = open(file, 'rb')
        bs = file.read(3)
        file.close()
        return bs == b'\xff\xd8\xff'
 
 
def is_gif(file):
        file = open(file, 'rb')
        bs = file.read(6)
        file.close()
        return bs == b'GIF89a'
