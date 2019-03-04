FROM rust:1.78.0
# Distributor ID: Debian
# Description:    Debian GNU/Linux 12 (bookworm)
# Release:        12
# Codename:       bookworm

RUN export TERM=xterm-256color

RUN apt update

# versions got from apt-cache policy <package>
RUN apt install -y vim=2:9.0.1378-2 \
        git=1:2.39.2-1.1 \
        lsb-release=12.0-1 \
        screen=4.9.0-4 \
        python3-opengl=3.1.6+dfsg-3 \
        python3-pyqt5=5.15.9+dfsg-1 \
        pylint=2.16.2-2 \
        cpplint=1.6.1-2 \
        lynx=2.9.0dev.12-1

# TODO: configure user
#--extension-pkg-whitelist=PyQt5.QtWidgets
RUN pylint --generate-rcfile > /root/.pylintrc
RUN sed -i 's/extension-pkg-allow-list=/extension-pkg-allow-list=PyQt5.QtWidgets/g' /root/.pylintrc
RUN sed -i 's/extension-pkg-whitelist=/extension-pkg-whitelist=PyQt5.QtWidgets/g' /root/.pylintrc

#QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root
RUN echo "export XDG_RUNTIME_DIR=/tmp/pyqt5_runtime" >> /root/.bashrc
RUN echo "export RUNLEVEL=3" >> /root/.bashrc

RUN cd /tmp && git clone https://github.com/KhronosGroup/OpenGL-Refpages.git
