all: localecompile
LNGS:=`find pretix_szamlazz/locale/ -mindepth 1 -maxdepth 1 -type d -printf "-l %f "`

localecompile:
	django-admin compilemessages

localegen:
	django-admin makemessages --keep-pot -i build -i dist -i "*egg*" $(LNGS)

xsd-gen:
	rm -rf pretix_szamlazz/szamlazz_types
	cd pretix_szamlazz && xsdata generate -c ../.xsdata.xml ../xsd

.PHONY: all localecompile localegen
