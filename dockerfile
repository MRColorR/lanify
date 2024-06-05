FROM debian:stable-slim



# Install necessary packages then clean up to reduce image size
RUN apt update && \
    apt upgrade -y && \
    apt install -qqy \
    curl \
    wget \
    git \
    chromium \
    chromium-driver \
    python3 \
    python3-requests\
    python3-selenium && \
    apt autoremove --purge -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*




# Install python requirements
COPY . .
ENTRYPOINT [ "python3", "main.py" ]