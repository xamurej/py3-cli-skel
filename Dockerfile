FROM python:3.5-onbuild
# Use the official python 3.5 image with docker's new onbuild technique.

CMD [ "./bin/cliapp" ]
