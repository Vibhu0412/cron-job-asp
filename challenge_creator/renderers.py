from rest_framework import renderers
import json


class ChallengeCreatorRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # response = ''

        # ErrorDetail will be there in auto generated errors.
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps(data)

        return response
