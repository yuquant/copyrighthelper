import os
import tempfile
import uuid
from fastapi import APIRouter, File, UploadFile, HTTPException
from starlette.responses import FileResponse

from copyright_helper import write_cleaned_code_to_doc
router = APIRouter()
TMP_FILE_ROOT = '/home/smit/PycharmProjects/copyrighthelper/copyright_helper_web/tmp_files'


@router.post('/code2doc')
async def create_file(file: UploadFile = File(..., content_type=["application/zip", "application/x-tar", "text/plain"])):
    ext = os.path.splitext(file.filename)[-1]
    content = await file.read()
    f_in = tempfile.NamedTemporaryFile(suffix=ext)
    with open(f_in.name, 'wb') as fb:
        fb.write(content)
    file_name = '{}.docx'.format(uuid.uuid4())
    f_out = '{}/{}'.format(TMP_FILE_ROOT, file_name)
    try:
        write_cleaned_code_to_doc(f_in.name, f_out)
    except ValueError as e:
        return HTTPException(status_code=403)
    headers = {'Content-Disposition': f'attachment; filename="{file_name}"'}
    return FileResponse(f_out, headers=headers, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
