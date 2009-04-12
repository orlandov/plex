VERSION = 1.1.5
TAR = ../plex-$(VERSION).tar
tar:	clean
	tar cvf $(TAR) *
	rm -f $(TAR).gz
	gzip $(TAR)

clean:
	rm -f */*.pyc *~ */*~ */*.dump tests/*.out2 tests/*.err
