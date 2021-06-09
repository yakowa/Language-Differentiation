# -=- Loading Dependencies -=-
from tkinter import Text, Label, Button, Tk, mainloop, END, INSERT, ttk, Scrollbar, LabelFrame, filedialog, messagebox, PhotoImage
from json import load, dump
from mpl import showBarChart, showCompBarChart
from googletrans import Translator, LANGUAGES
import os
from base64 import b64decode


# -=- Initializing Global Variables -=-
global cacheComp, cacheSwitch, __version__
cacheComp = None
cacheSwitch = "l"
__version__ = "v2.3.2"


# -=- Gui Set up -=-
# $ Base TKinter code
root = Tk()
root.title('Language Differentiation')
icon = """AAABAAQAGBgAAAEAIACICQAARgAAABAQAAABACAAaAQAAM4JAAAgIAAAAQAgAKgQAAA2DgAAQEAAAAEAIAAoQgAA3h4AACgAAAAYAAAAMAAAAAEAIAAAAAAAYAkAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHdAcHB9cHBwf/BwcH/wcHB/8HBwf/BwcH/wcHCP8HBwj/BwcI/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwfXBwcHdAAAAAAHBwd0BwcH/wcHB/8HBwf/BwcH/wgKDv8KGTP/DzR4/xs7q/8vJ8D/LyfA/yQfj/8bF2X/Dw0r/wgICv8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB3QHBwfXBwcH/wcHB/8HCQ3/Di1l/xVWzf8YZ/b/GGf2/xlm9v81OfT/OjD0/zow9P86MPT/OC/s/ykipf8MCx7/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB9cHBwf/BwcH/wgMFP8TS6//GGf2/xhn9v8YZ/b/GGf2/xhn9v8iV/X/OjD0/zow9P86MPT/OjD0/zow9P8vJ8L/Cwoa/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/w0oWf8YZvT/GGf2/xhn9v8YZ/b/GGf2/xhn9v8YZ/b/Mjz0/zow9P86MPT/OjD0/zow9P86MPT/KSOm/wgHCv8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcJDP8RQJX/GGf2/xhn9v8YZ/b/GGf2/xhm9f8YZvP/H1z2/zow9P86MPT/OjD0/zow9P86MPT/OC/t/xEPNP8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8IDBL/FE+6/xhn9v8XZO//Dzd+/wobOP8JEyX/DjBu/y095v86MPT/OjD0/zow9P86MPT/OjD0/x8beP8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CRIi/xVUyP8MJlT/BwcI/wcHB/8HBwf/BwcH/xYsfv86MPT/OjD0/zow9P86MPT/OjD0/zMopf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgNFv8HBwj/BwcH/wcHB/8HBwf/BwcH/xEVQv86MPT/OjD0/zow9P86MPT/UTzi/35Pdf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xEPN/85L/T/OjD0/zow9P9RPOL/q2uZ/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xEPN/85L/T/OjD0/1A84v+ra5n/tXCR/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xEPN/85L/T/UDzi/6trmf+1cJH/tXCR/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xEPN/9QO+L/rGuZ/7Vwkf+1cJH/tXCR/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/yUbKv+sa5f/tXCR/7Vwkf+1cJH/tXCR/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/z0qBf/ZjiH/vnh0/7Vwkf+1cJH/tXCR/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/z0qBf/jlwD/45cA/9WLLP/Ce2j/tnGP/4hVbf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/z0qBf/jlwD/45cA/+OXAP/jlwD/3pIR/6BoP/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CQkH/wkJB/8JCQf/CQkH/z4sBf/jlwD/45cA/+OX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B/8VEkj/OS/0/zow9P86MPT/OzHz/4hYtv+1cJH/tXCR/3lMYf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xUSSP85L/T/OjD0/zwx8/+HWLb/tXCR/7Vwkf+1cJH/eUxh/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/FRJI/zkv9P87MPP/h1i2/7Vwkf+1cJH/tXCR/7Vwkf95TGH/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8VEkj/OzDy/4dYtv+1cJH/tXCR/7Vwkf+1cJH/tXCR/3lMYf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/xYSR/+HWLX/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/eUxh/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/SzIZ/754df+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf95TGH/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/9PNgX/4ZUG/82ERv+5c4b/tXCR/7Vwkf+1cJH/tXCR/3lMYf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/082Bf/jlwD/45cA/+CVCf/NhEf/unSB/7Vwkf+1cJH/eUxh/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/TzYF/+OXAP/jlwD/45cA/+OXAP/ilgL/14wn/8R9Yf95TGH/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/9PNgX/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/6txF/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wkJB/8KCgj/CgoI/woKCP8KCgj/CgoI/1E4Bf/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/tXgD/wgIB/8ICAf/CAgH/wgIB/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/Y2Ie/4eGKP+Hhij/h4Yo/4eGKP+Hhij/l48n/9GkFv/imAL/45cA/+OXAP/jlwD/45cA/+OXAP/JhgH/fFMD/3xTA/98UwP/fFMD/0QvBf8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgIB/+HhSj/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7yzMP/RpBb/4ZgC/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/eFED/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/4eFKP+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+9si//z6YZ/9+aBf/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP94UQP/BwcH/wcHB/8HBwf/BwcH+wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAf/h4Uo/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2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8f+UXqf/Pykz/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgNFv8IDRX/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HCg7/HySM/zow9P86MPT/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/0E07v+TXqz/sm6P/z8pM/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwkM/yAhi/85L/T/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/0Ez7/+SXq3/tXCR/7Juj/8/KTP/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8iHIj/OC7z/zow9P86MPT/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/z8z8P+UX6v/tXCR/7Vwkf+ybo//Pykz/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/IhyI/zgu8/86MPT/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/0Ez7/+VYKr/tXCR/7Vwkf+1cJH/sm6P/z8pM/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/yIciP84LvP/OjD0/zow9P86MPT/OjD0/zow9P86MPT/OjD0/0E07v+UXqz/tXCR/7Vwkf+1cJH/tXCR/7Juj/8/KTP/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8iHIj/OC7z/zow9P86MPT/OjD0/zow9P86MPT/OjD0/0Az7/+UX6v/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/IhyI/zgu8/86MPT/OjD0/zow9P86MPT/OjD0/z4y8f+WYKr/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/sm6P/0ApM/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/yIciP84LvP/OjD0/zow9P86MPT/OjD0/0E07v+TX6z/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Juj/9AKTP/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8iHIj/OC7z/zow9P86MPT/OjD0/0I07f+SXq3/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/IhyI/zgu8/86MPT/OjD0/z0y8v+UX6v/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/sm6P/0ApM/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/yIciP84LvP/OjD0/0Az7/+WYKr/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Juj/9AKTP/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8iHIj/OC7z/0E07v+SXq3/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/IhyI/0Ay7f+SXq3/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/sm6P/0ApM/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/ycfh/+WYKn/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Juj/9AKTP/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/+FVFb/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/l2UC/9WLLv+5dIP/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/sm6P/0ApM/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/5dlAv/jlwD/25AZ/8J7Z/+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Juj/9AKTP/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/+XZQL/45cA/+OXAP/jlwH/2I4h/8J7af+2cY3/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/l2UC/+OXAP/jlwD/45cA/+OXAP/jlwD/2I4j/8J7Z/+1cJH/tXCR/7Vwkf+1cJH/tXCR/7Vwkf+1cJH/sm6P/0ApM/8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/5dlAv/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/140k/8V+Xf+4c4b/tXCR/7Vwkf+1cJH/tXCR/7Juj/9AKTP/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/+XZQL/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/4JQJ/9aMKv+/eHL/tnGN/7Vwkf+ybo//QCkz/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/l2UC/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/96TEf/IgFT/s2+P/0EqNf8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/5dlAv/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/9WLLf9uSCr/CAcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/+XZQL/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/hlkG/wgHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/l2UC/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/4ZZBv8IBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CQkH/wwMCP8MDAj/DAwI/wwMCP8MDAj/DAwI/wwMCP8MDAj/DAwI/wwMCP8MDAj/DAwI/5hmAv/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP+GWQb/CggH/wkIBv8JCAb/CQgG/wkIBv8JCAb/CQgG/wkIBv8JCAb/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/yopEP9ZWBv/WVgb/1lYG/9ZWBv/WVgb/1lYG/9ZWBv/WVgb/1lYG/9ZWBv/WVgb/1lYG/+XfRf/3JsI/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/hloD/yQaBf8kGgX/JBoF/yQaBf8kGgX/JBoF/yQaBf8kGgX/JBoF/wwKBv8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgIB/9UUxv/tbM0/7WzNP+1szT/tbM0/7WzNP+1szT/tbM0/7WzNP+1szT/tbM0/7WzNP+1szT/trQ0/7q0Mv/JqiD/3poG/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/9qRAP/TjQD/040A/9ONAP/TjQD/040A/9ONAP/TjQD/040A/9GLAf8PDAf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAf/VVUb/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/JqR//3psH/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/glQD/DwwH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/1VVG/+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7q0Mv/KqR//3JwI/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/4JUA/w8MB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgIB/9VVRv/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7u0Mf/JqSD/3ZsH/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+CVAP8PDAf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAf/VVUb/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7m1NP/AsCv/1qEQ/+KYAv/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/glQD/DwwH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/wHBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/1VVG/+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/Bryr/1aER/+KYAv/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/4JUA/w8MB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/wHBwfpBwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgIB/9VVRv/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/BsCv/1qEQ/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+CVAP8PDAf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwfpBgYGxQcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAf/VVUb/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2NP/BsCr/1qAQ/+OXAP/jlwD/45cA/+OXAP/jlwD/45cA/+OXAP/glQD/DwwH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BgYGxQcHB44HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/1VVG/+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/BsCv/1aER/+GYAv/jlwD/45cA/+OXAP/jlwD/4JUA/w8MB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB44ICAhCBwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wgIB/9VVRv/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/Bryr/1aES/+OXAf/jlwD/45cA/+CVAP8PDAf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAhCAAAAAAcHB8QHBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8ICAf/VVUb/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf+4tjX/uLY1/7i2Nf/BsCr/1qAQ/+OXAP/glQD/DwwH/wcHB/8HBwf/BwcH/wcHB/8HBwfEAAAAAAAAAAAICAhABwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/0RDFv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI8q/5CPKv+Qjyr/kI4q/5COKv+Qjir/kI4q/5COKv+Qjir/kI4q/5COKv+YiCD/o34Q/xcVCv8HBwf/BwcH/wcHB/8HBwf/CAgIQAAAAAAAAAAAAAAAAAgICGIHBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8ICAf/CAgH/wgIB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/CAgIYgAAAAAAAAAAAAAAAAAAAAAAAAAACAgIQAcHB8QHBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwfECAgIQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgIQgcHB44GBgbFBwcH6QcHB/wHBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/8HBwf/BwcH/wcHB/wHBwfpBgYGxQcHB44ICAhCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="""
icondata= b64decode(icon)
## The temp file is icon.ico
tempFile = "icon.ico"
iconfile = open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()
root.wm_iconbitmap(tempFile)
## Delete the tempfile
os.remove(tempFile)
# root.iconbitmap("jacobem.ico")
root.resizable(False, False)





# -=- Initializing Objects -=-
# $ Text Type Object
class TextObject:
    def __init__(self, text):
        # Setting class values
        self.text = text

        # Making a dictonary of the amount of letters in a TextObejct
        self.allowedChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
        self.list = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
        for char in self.text:
            if char.upper() in self.allowedChars:
                formatedChar = str(char)
                self.list[formatedChar.upper()] += 1




# -=- Functions -=-
# $ Open file and import text...
def openFile():
    try:
        filename = filedialog.askopenfilename(initialdir='C:/Users/User/Desktop/', title='Import File...', filetypes=(('Text Documents', '*.txt'), ('Yako Files', '*.yako')))
        rawFile = open(filename, "r")
        inputField.insert("1.0", rawFile.read())
        rawFile.close()
    except:
        messagebox.showerror('Error!', "If you see this error, it will be fixed soon.")

# $ Get input field as object function
def getInputField():
    return TextObject(inputField.get("1.0", END))

# BUTTON FUNCS
# displayLetterFrequency, detectLanguage, displayCompareLanguages, caseSwitch, getAsList, saveAsJSON

# $ Letter frequency graphing function
def displayLetterFrequency():
    # Getting the input field as a TextObject object
    textObject = getInputField()
    # Custom module made for displaying graphs.
    # In this example, displaying the alphabet with the frequency of the object.
    showBarChart("alpha", textObject.list)


# $ Detect language function
def detectLanguage(show=True):
    # Getting the input field as a TextObject object
    textObject = getInputField()
    # Loading a google translator
    translator = Translator()
    # Translate the inputfield's text
    result = translator.translate(textObject.text)
    # Formatting the detected language
    resultLang = result.src
    langWord = LANGUAGES[resultLang]
    langWord = langWord.capitalize()
    # Display the detected language
    if show:
        messagebox.showinfo('Detected language!', f'Detected language: {langWord}.')
    else:
        return langWord


# $ Display compare languages
def displayCompareLanguages():
    global cacheComp
    cacheComp = cacheComp
    if cacheComp == None:
        # Getting the input field as a TextObject object
        textObject = getInputField()
        # Caching the object
        cacheComp = textObject
        # Clearing the input field
        inputField.delete("1.0", END)
        # Displaying a confirmation message
        messagebox.showinfo('Compare Langauges!', 'Item one for comparison has been saved. Please enter item two into the input field and click compare langauge again to view graph.')
    # If there is item one saved in the cache
    else:
        # Set both items
        compOne = cacheComp
        compTwo = getInputField()
        # Clear the cache
        cacheComp = None
        # Custom module made for displaying graphs.
        # In this example, displaying the alphabet with the comparison between the two input objects.
        showCompBarChart("alpha", compOne.list, "alpha", compTwo.list)


# $ Switch case of input
def caseSwitch():
    global cacheSwitch
    cacheSwitch = cacheSwitch
    if cacheSwitch == "l":
        # Getting the input field as a TextObject object
        textObject = getInputField()
        # Getting the text in upper case
        text = textObject.text.upper()
        # Removing all break lines
        text = text.rstrip("\n")
        # Clearing the input field
        inputField.delete("1.0", END)
        # Setting the input field
        inputField.insert("1.0", text)
        # Caching as upper case
        cacheSwitch = "u"
    else:
        # Getting the input field as a TextObject object
        textObject = getInputField()
        # Getting the text in lower case
        text = textObject.text.lower()
        # Removing all break lines
        text = text.rstrip("\n")
        # Clearing the input field
        inputField.delete("1.0", END)
        # Setting the input field
        inputField.insert("1.0", text)
        # Caching as upper case
        cacheSwitch = "l"


# $ Get the input as a python list
def getLength():
    try:
        # Getting objects + vars
        textObject = getInputField()
        text = textObject.text
        text = text.rstrip("\n")
        # Displaying success message
        messagebox.showinfo('Success!', f'Your inputted text is {len(text)} characters long!')
    except Exception as error:
        # Displaying error message
        messagebox.showerror('Error!', error)


# $ Saving to DB function
def saveAsJSON():
    try:
        # Getting objects + vars
        textObject = getInputField()
        lang = detectLanguage(show=False)
        text = textObject.text
        rawJson = {"detected_language": lang, "text": text}
        # Saving json to clipboard
        root.clipboard_clear()
        root.clipboard_append(rawJson)
        root.update()
        # Displaying success message
        messagebox.showinfo('Success!', f'Saved word element to your clipboard!')
    except Exception as error:
        # Displaying error message
        messagebox.showerror('Error!', error)
#




# -=- Setting up the TKinter GUI -=-

# $ Title
Label(root, text='Language Differentiation', font='Roboto 30').grid(row=0, column=0, columnspan=3, pady=(20, 20))

# $ Inputs
# Frame
inputFrame = LabelFrame(root, text="Input", padx=10, pady=10)
inputFrame.grid(row=1, column=0, columnspan=3, padx=(35, 35), pady=(0, 20))

# Load file
Button(inputFrame, text="Import Text File...", command=openFile, width=40, height=2).grid(row=0, column=0, columnspan=3, padx=(35, 35), pady=(0, 20), sticky="ew")
# Textbox
inputField = Text(inputFrame, font='Verdana 15', width=40, height=10)
# Scrollbar
inputFieldScrollBar = Scrollbar(inputFrame, orient="vertical", command=inputField.yview)
# configs + adding to grid
inputField.configure(yscrollcommand=inputFieldScrollBar.set)
inputField.grid(row=1, column=0, padx=(35, 35), pady=(0, 20), sticky="nsew")
inputFieldScrollBar.grid(row=1, column=1, padx=(0, 35), pady=(0, 20), sticky="nsew")
# configs + adding to grid


# $ Buttons
# displayLetterFrequency, detectLanguage, displayCompareLanguages, caseSwitch, getAsList, saveAsJSON
Button(root, command=displayLetterFrequency, text='Letter Frequency', font='Verdana 13').grid(row=3, column=0, padx=(35, 5), pady=(0, 20))
Button(root, command=detectLanguage, text='Detect Language', font='Verdana 13').grid(row=3, column=1, padx=(5, 5), pady=(0, 20))
Button(root, command=displayCompareLanguages, text='Compare Languages', font='Verdana 13').grid(row=3, column=2, padx=(5, 35), pady=(0, 20))
Button(root, command=caseSwitch, text='Case Switch', font='Verdana 13').grid(row=4, column=0, padx=(35, 5), pady=(0, 20))
Button(root, command=getLength, text='Get Length', font='Verdana 13').grid(row=4, column=1, padx=(5, 5), pady=(0, 20))
Button(root, command=saveAsJSON, text='Save As JSON', font='Verdana 13').grid(row=4, column=2, padx=(5, 35), pady=(0, 20))

Label(root, text='Made by JacobEM.com', font='Roboto 13', fg="#070707").grid(row=6, column=0, padx=(5, 5), pady=(0, 10), sticky="sw")
Label(root, text=f'Language Differentiation {__version__}', font='Roboto 13', fg="#070707").grid(row=5, column=2, padx=(5, 5), pady=(10, 0), sticky="se")
Label(root, text='is licensed under CC BY-NC-ND 4.0', font='Roboto 13', fg="#070707").grid(row=6, column=2, padx=(5, 5), pady=(0, 10), sticky="se")



# -=- Running the mainloop -=-
root.mainloop()