FROM python:latest

COPY . /cms

WORKDIR . /cms

RUN pip install aiosqlite
RUN pip install annotated-types
RUN pip install anyio
RUN pip install click
RUN pip install colorama
RUN pip install ecdsa
RUN pip install fastapi
RUN pip install greenlet
RUN pip install h11
RUN pip install idna
RUN pip install passlib
RUN pip install pyasn1
RUN pip install pydantic
RUN pip install pydantic_core
RUN pip install PyJWT
RUN pip install python-jose
RUN pip install python-multipart
RUN pip install rsa
RUN pip install six
RUN pip install sniffio
RUN pip install SQLAlchemy
RUN pip install starlette
RUN pip install typing_extensions
RUN pip install uvicorn


CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2525"]