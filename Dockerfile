FROM mcr.microsoft.com/playwright:focal
RUN pip3 install pytest-playwright
RUN playwright install-deps
WORKDIR /playwright_sample
COPY . .
RUN pytest --video on \
    --output evidences --slowmo 150 \
    --browser chromium --browser firefox \
    --screenshot on