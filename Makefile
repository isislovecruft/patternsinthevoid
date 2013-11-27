PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
# Everything from EXTRAS_DIR will be copied to the root directory of the
# webserver:
EXTRAS_DIR=$(BASEDIR)/content/extra

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=106.187.37.158
SSH_PORT=22
SSH_USER=isis
SSH_TARGET_DIR=published

RSYNC_TARGET_DIR=published
RSYNC_LOGFILE=$(BASEDIR)/update.log

# Store a passphrase, without an newline after it (it must also be properly
# shell-escaped), in this file, so that we can ssh in as a normal user and use
# sudo for any chmod/chown scripts we need to run to get the website files
# into place with the appropriate permissions:
REMOTE_PASSWORD:=$(shell cat $(BASEDIR)/passwd.private)

# See https://code.patternsinthevoid.net/?p=scripts.git;a=blob;f=move-blog-dirs.sh;hb=HEAD
# for an example of what this variable is used for
REMOTE_SUDO_SCRIPT=/home/$(SSH_USER)/scripts/move-blog-dirs.sh

GITHUB_REMOTE_NAME=isislovecruft

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   ssh_upload                       upload the web site via SSH        '
	@echo '   rsync_upload                     upload the web site via rsync+ssh  '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '                                                                       '


html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

devserver:
	$(BASEDIR)/develop_server.sh restart

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

#ssh_upload: publish
#	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	@ssh $(SSH_USER)@$(SSH_HOST) mkdir -p ~/published
	@echo "\nrsyncing ${OUTPUTDIR} to ${SSH_HOST}:${SSH_TARGET_DIR}...\n"
	rsync -e "ssh -p $(SSH_PORT)" -rthLvz --protect-args \
		--safe-links --chmod=go=rX --chmod=u=rwX \
		--cvs-exclude --exclude '*~' \
		--delete-during --delete-excluded \
		--force --prune-empty-dirs \
		--log-file=$(RSYNC_LOGFILE) \
		$(OUTPUTDIR)/ $(EXTRAS_DIR)/ \
		$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)/
	@ssh -p $(SSH_PORT) $(SSH_USER)@$(SSH_HOST) "echo $(REMOTE_PASSWORD) | \
		sudo -S $(REMOTE_SUDO_SCRIPT)"

upload: rsync_upload

github: publish
	ghp-import $(OUTPUTDIR)
	git push $(GITHUB_REMOTE_NAME) gh-pages

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload github
