%define _prefix /usr/local/php

Name:		php
Version:	5.6.5
Release:	1%{?dist}
Summary:	php-fpm

Group:		Applications/Internet
License:	GPLv2+
URL:		http://www.php.net
Source0:    php-5.6.5.tar.gz
Source1:	init.d.php-fpm
Source2:    php.ini
Source3:    php-fpm.conf

Requires:	mysql-devel

%description


%prep
%setup -q


%build
./configure \
--prefix=/usr/local/%{name}-%{version} \
--with-config-file-path=/usr/local/%{name}-%{version}/etc \
--with-libdir=/lib64 \
--with-mysql \
--with-mysqli \
--with-pdo-mysql \
--with-zlib \
--with-curl \
--with-mcrypt \
--with-gd \
--with-jpeg-dir \
--with-png-dir \
--with-freetype-dir \
--with-openssl \
--with-mhash \
--with-ldap \
--disable-rpath \
--disable-ipv6 \
--enable-fpm \
--enable-gd-native-ttf \
--enable-sockets \
--enable-mbregex \
--enable-mbstring \
--enable-zip \
--enable-soap \
--enable-bcmath \
--enable-calendar \
--enable-opcache \
--enable-inline-optimization \
--enable-maintainer-zts

make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install
rm -rf %{buildroot}/usr/local/%{name}-%{version}/{.channels,.depdb,.depdblock,.filemap,.lock,.registry}
rm -rf %{buildroot}/usr/local/{.channels,.depdb,.depdblock,.filemap,.lock,.registry}
rm -rf %{buildroot}/{.channels,.depdb,.depdblock,.filemap,.lock,.registry}
rm -rf %{buildroot}/usr/local/%{name}-%{version}/lib/php/.channels/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/lib/php/.registry/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/lib/php/.channels/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/lib/php/doc/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/lib/php/test/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/php/man/
rm -rf %{buildroot}/usr/local/%{name}-%{version}/bin/phar
rm -rf %{buildroot}/usr/local/%{name}-%{version}/etc/php-fpm.conf.default
mkdir -p %{buildroot}/usr/local/%{name}-%{version}/var/{log,run}
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}/usr/local/%{name}-%{version}/sbin/init.d.php-fpm
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}/usr/local/%{name}-%{version}/etc/php.ini
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}/usr/local/%{name}-%{version}/etc/php-fpm.conf

%files
%defattr(-,root,root)
/usr/local/php-5.6.5/var/log
/usr/local/php-5.6.5/var/run
/usr/local/php-5.6.5/bin/pear
/usr/local/php-5.6.5/bin/peardev
/usr/local/php-5.6.5/bin/pecl
/usr/local/php-5.6.5/bin/phar.phar
/usr/local/php-5.6.5/bin/php
/usr/local/php-5.6.5/bin/php-cgi
/usr/local/php-5.6.5/bin/php-config
/usr/local/php-5.6.5/bin/phpize
/usr/local/php-5.6.5/etc/pear.conf
/usr/local/php-5.6.5/etc/php-fpm.conf
/usr/local/php-5.6.5/etc/php.ini
/usr/local/php-5.6.5/include/php/TSRM/TSRM.h
/usr/local/php-5.6.5/include/php/TSRM/readdir.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_config.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_config.w32.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_config_common.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_nw.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_strtok_r.h
/usr/local/php-5.6.5/include/php/TSRM/tsrm_win32.h
/usr/local/php-5.6.5/include/php/Zend/zend.h
/usr/local/php-5.6.5/include/php/Zend/zend_API.h
/usr/local/php-5.6.5/include/php/Zend/zend_alloc.h
/usr/local/php-5.6.5/include/php/Zend/zend_ast.h
/usr/local/php-5.6.5/include/php/Zend/zend_build.h
/usr/local/php-5.6.5/include/php/Zend/zend_builtin_functions.h
/usr/local/php-5.6.5/include/php/Zend/zend_closures.h
/usr/local/php-5.6.5/include/php/Zend/zend_compile.h
/usr/local/php-5.6.5/include/php/Zend/zend_config.h
/usr/local/php-5.6.5/include/php/Zend/zend_config.nw.h
/usr/local/php-5.6.5/include/php/Zend/zend_config.w32.h
/usr/local/php-5.6.5/include/php/Zend/zend_constants.h
/usr/local/php-5.6.5/include/php/Zend/zend_dtrace.h
/usr/local/php-5.6.5/include/php/Zend/zend_dynamic_array.h
/usr/local/php-5.6.5/include/php/Zend/zend_errors.h
/usr/local/php-5.6.5/include/php/Zend/zend_exceptions.h
/usr/local/php-5.6.5/include/php/Zend/zend_execute.h
/usr/local/php-5.6.5/include/php/Zend/zend_extensions.h
/usr/local/php-5.6.5/include/php/Zend/zend_float.h
/usr/local/php-5.6.5/include/php/Zend/zend_gc.h
/usr/local/php-5.6.5/include/php/Zend/zend_generators.h
/usr/local/php-5.6.5/include/php/Zend/zend_globals.h
/usr/local/php-5.6.5/include/php/Zend/zend_globals_macros.h
/usr/local/php-5.6.5/include/php/Zend/zend_hash.h
/usr/local/php-5.6.5/include/php/Zend/zend_highlight.h
/usr/local/php-5.6.5/include/php/Zend/zend_indent.h
/usr/local/php-5.6.5/include/php/Zend/zend_ini.h
/usr/local/php-5.6.5/include/php/Zend/zend_ini_parser.h
/usr/local/php-5.6.5/include/php/Zend/zend_ini_scanner.h
/usr/local/php-5.6.5/include/php/Zend/zend_ini_scanner_defs.h
/usr/local/php-5.6.5/include/php/Zend/zend_interfaces.h
/usr/local/php-5.6.5/include/php/Zend/zend_istdiostream.h
/usr/local/php-5.6.5/include/php/Zend/zend_iterators.h
/usr/local/php-5.6.5/include/php/Zend/zend_language_parser.h
/usr/local/php-5.6.5/include/php/Zend/zend_language_scanner.h
/usr/local/php-5.6.5/include/php/Zend/zend_language_scanner_defs.h
/usr/local/php-5.6.5/include/php/Zend/zend_list.h
/usr/local/php-5.6.5/include/php/Zend/zend_llist.h
/usr/local/php-5.6.5/include/php/Zend/zend_modules.h
/usr/local/php-5.6.5/include/php/Zend/zend_multibyte.h
/usr/local/php-5.6.5/include/php/Zend/zend_multiply.h
/usr/local/php-5.6.5/include/php/Zend/zend_object_handlers.h
/usr/local/php-5.6.5/include/php/Zend/zend_objects.h
/usr/local/php-5.6.5/include/php/Zend/zend_objects_API.h
/usr/local/php-5.6.5/include/php/Zend/zend_operators.h
/usr/local/php-5.6.5/include/php/Zend/zend_ptr_stack.h
/usr/local/php-5.6.5/include/php/Zend/zend_qsort.h
/usr/local/php-5.6.5/include/php/Zend/zend_signal.h
/usr/local/php-5.6.5/include/php/Zend/zend_stack.h
/usr/local/php-5.6.5/include/php/Zend/zend_static_allocator.h
/usr/local/php-5.6.5/include/php/Zend/zend_stream.h
/usr/local/php-5.6.5/include/php/Zend/zend_string.h
/usr/local/php-5.6.5/include/php/Zend/zend_strtod.h
/usr/local/php-5.6.5/include/php/Zend/zend_ts_hash.h
/usr/local/php-5.6.5/include/php/Zend/zend_types.h
/usr/local/php-5.6.5/include/php/Zend/zend_variables.h
/usr/local/php-5.6.5/include/php/Zend/zend_virtual_cwd.h
/usr/local/php-5.6.5/include/php/Zend/zend_vm.h
/usr/local/php-5.6.5/include/php/Zend/zend_vm_def.h
/usr/local/php-5.6.5/include/php/Zend/zend_vm_execute.h
/usr/local/php-5.6.5/include/php/Zend/zend_vm_opcodes.h
/usr/local/php-5.6.5/include/php/ext/date/lib/timelib.h
/usr/local/php-5.6.5/include/php/ext/date/lib/timelib_config.h
/usr/local/php-5.6.5/include/php/ext/date/lib/timelib_structs.h
/usr/local/php-5.6.5/include/php/ext/date/php_date.h
/usr/local/php-5.6.5/include/php/ext/dom/xml_common.h
/usr/local/php-5.6.5/include/php/ext/ereg/php_ereg.h
/usr/local/php-5.6.5/include/php/ext/ereg/php_regex.h
/usr/local/php-5.6.5/include/php/ext/ereg/regex/cclass.h
/usr/local/php-5.6.5/include/php/ext/ereg/regex/cname.h
/usr/local/php-5.6.5/include/php/ext/ereg/regex/regex.h
/usr/local/php-5.6.5/include/php/ext/ereg/regex/regex2.h
/usr/local/php-5.6.5/include/php/ext/ereg/regex/utils.h
/usr/local/php-5.6.5/include/php/ext/filter/php_filter.h
/usr/local/php-5.6.5/include/php/ext/gd/gd_compat.h
/usr/local/php-5.6.5/include/php/ext/gd/gdcache.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gd.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gd_intern.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gd_io.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdcache.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdfontg.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdfontl.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdfontmb.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdfonts.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdfontt.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/gdhelpers.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/jisx0208.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/wbmp.h
/usr/local/php-5.6.5/include/php/ext/gd/libgd/webpimg.h
/usr/local/php-5.6.5/include/php/ext/gd/php_gd.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_adler32.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_crc32.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_fnv.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_gost.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_haval.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_joaat.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_md.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_ripemd.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_sha.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_snefru.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_tiger.h
/usr/local/php-5.6.5/include/php/ext/hash/php_hash_whirlpool.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_have_bsd_iconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_have_glibc_iconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_have_ibm_iconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_have_iconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_have_libiconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_iconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_iconv_aliased_libiconv.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_iconv_supports_errno.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_php_iconv_h_path.h
/usr/local/php-5.6.5/include/php/ext/iconv/php_php_iconv_impl.h
/usr/local/php-5.6.5/include/php/ext/json/php_json.h
/usr/local/php-5.6.5/include/php/ext/libxml/php_libxml.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/config.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/eaw_table.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfilter.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_8bit.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_pass.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_wchar.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_allocators.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_consts.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_convert.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_defs.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_encoding.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_filter_output.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_ident.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_language.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_memory_device.h
/usr/local/php-5.6.5/include/php/ext/mbstring/libmbfl/mbfl/mbfl_string.h
/usr/local/php-5.6.5/include/php/ext/mbstring/mbstring.h
/usr/local/php-5.6.5/include/php/ext/mbstring/oniguruma/oniguruma.h
/usr/local/php-5.6.5/include/php/ext/mbstring/php_mbregex.h
/usr/local/php-5.6.5/include/php/ext/mbstring/php_onig_compat.h
/usr/local/php-5.6.5/include/php/ext/mysqli/mysqli_mysqlnd.h
/usr/local/php-5.6.5/include/php/ext/mysqli/php_mysqli_structs.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/config-win.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_alloc.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_block_alloc.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_charset.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_debug.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_enum_n_def.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_ext_plugin.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_libmysql_compat.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_net.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_portability.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_priv.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_result.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_result_meta.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_reverse_api.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_statistics.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_structs.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/mysqlnd_wireprotocol.h
/usr/local/php-5.6.5/include/php/ext/mysqlnd/php_mysqlnd.h
/usr/local/php-5.6.5/include/php/ext/pcre/pcrelib/config.h
/usr/local/php-5.6.5/include/php/ext/pcre/pcrelib/pcre.h
/usr/local/php-5.6.5/include/php/ext/pcre/pcrelib/pcre_internal.h
/usr/local/php-5.6.5/include/php/ext/pcre/pcrelib/pcreposix.h
/usr/local/php-5.6.5/include/php/ext/pcre/pcrelib/ucp.h
/usr/local/php-5.6.5/include/php/ext/pcre/php_pcre.h
/usr/local/php-5.6.5/include/php/ext/pdo/php_pdo.h
/usr/local/php-5.6.5/include/php/ext/pdo/php_pdo_driver.h
/usr/local/php-5.6.5/include/php/ext/pdo/php_pdo_error.h
/usr/local/php-5.6.5/include/php/ext/phar/php_phar.h
/usr/local/php-5.6.5/include/php/ext/session/mod_files.h
/usr/local/php-5.6.5/include/php/ext/session/mod_user.h
/usr/local/php-5.6.5/include/php/ext/session/php_session.h
/usr/local/php-5.6.5/include/php/ext/simplexml/php_simplexml.h
/usr/local/php-5.6.5/include/php/ext/simplexml/php_simplexml_exports.h
/usr/local/php-5.6.5/include/php/ext/sockets/php_sockets.h
/usr/local/php-5.6.5/include/php/ext/spl/php_spl.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_array.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_directory.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_dllist.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_engine.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_exceptions.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_fixedarray.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_functions.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_heap.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_iterators.h
/usr/local/php-5.6.5/include/php/ext/spl/spl_observer.h
/usr/local/php-5.6.5/include/php/ext/sqlite3/libsqlite/sqlite3.h
/usr/local/php-5.6.5/include/php/ext/standard/base64.h
/usr/local/php-5.6.5/include/php/ext/standard/basic_functions.h
/usr/local/php-5.6.5/include/php/ext/standard/crc32.h
/usr/local/php-5.6.5/include/php/ext/standard/credits.h
/usr/local/php-5.6.5/include/php/ext/standard/credits_ext.h
/usr/local/php-5.6.5/include/php/ext/standard/credits_sapi.h
/usr/local/php-5.6.5/include/php/ext/standard/crypt_blowfish.h
/usr/local/php-5.6.5/include/php/ext/standard/crypt_freesec.h
/usr/local/php-5.6.5/include/php/ext/standard/css.h
/usr/local/php-5.6.5/include/php/ext/standard/cyr_convert.h
/usr/local/php-5.6.5/include/php/ext/standard/datetime.h
/usr/local/php-5.6.5/include/php/ext/standard/dl.h
/usr/local/php-5.6.5/include/php/ext/standard/exec.h
/usr/local/php-5.6.5/include/php/ext/standard/file.h
/usr/local/php-5.6.5/include/php/ext/standard/flock_compat.h
/usr/local/php-5.6.5/include/php/ext/standard/fsock.h
/usr/local/php-5.6.5/include/php/ext/standard/head.h
/usr/local/php-5.6.5/include/php/ext/standard/html.h
/usr/local/php-5.6.5/include/php/ext/standard/html_tables.h
/usr/local/php-5.6.5/include/php/ext/standard/info.h
/usr/local/php-5.6.5/include/php/ext/standard/md5.h
/usr/local/php-5.6.5/include/php/ext/standard/microtime.h
/usr/local/php-5.6.5/include/php/ext/standard/pack.h
/usr/local/php-5.6.5/include/php/ext/standard/pageinfo.h
/usr/local/php-5.6.5/include/php/ext/standard/php_array.h
/usr/local/php-5.6.5/include/php/ext/standard/php_assert.h
/usr/local/php-5.6.5/include/php/ext/standard/php_browscap.h
/usr/local/php-5.6.5/include/php/ext/standard/php_crypt.h
/usr/local/php-5.6.5/include/php/ext/standard/php_crypt_r.h
/usr/local/php-5.6.5/include/php/ext/standard/php_dir.h
/usr/local/php-5.6.5/include/php/ext/standard/php_dns.h
/usr/local/php-5.6.5/include/php/ext/standard/php_ext_syslog.h
/usr/local/php-5.6.5/include/php/ext/standard/php_filestat.h
/usr/local/php-5.6.5/include/php/ext/standard/php_fopen_wrappers.h
/usr/local/php-5.6.5/include/php/ext/standard/php_ftok.h
/usr/local/php-5.6.5/include/php/ext/standard/php_http.h
/usr/local/php-5.6.5/include/php/ext/standard/php_image.h
/usr/local/php-5.6.5/include/php/ext/standard/php_incomplete_class.h
/usr/local/php-5.6.5/include/php/ext/standard/php_iptc.h
/usr/local/php-5.6.5/include/php/ext/standard/php_lcg.h
/usr/local/php-5.6.5/include/php/ext/standard/php_link.h
/usr/local/php-5.6.5/include/php/ext/standard/php_mail.h
/usr/local/php-5.6.5/include/php/ext/standard/php_math.h
/usr/local/php-5.6.5/include/php/ext/standard/php_metaphone.h
/usr/local/php-5.6.5/include/php/ext/standard/php_password.h
/usr/local/php-5.6.5/include/php/ext/standard/php_rand.h
/usr/local/php-5.6.5/include/php/ext/standard/php_smart_str.h
/usr/local/php-5.6.5/include/php/ext/standard/php_smart_str_public.h
/usr/local/php-5.6.5/include/php/ext/standard/php_standard.h
/usr/local/php-5.6.5/include/php/ext/standard/php_string.h
/usr/local/php-5.6.5/include/php/ext/standard/php_type.h
/usr/local/php-5.6.5/include/php/ext/standard/php_uuencode.h
/usr/local/php-5.6.5/include/php/ext/standard/php_var.h
/usr/local/php-5.6.5/include/php/ext/standard/php_versioning.h
/usr/local/php-5.6.5/include/php/ext/standard/proc_open.h
/usr/local/php-5.6.5/include/php/ext/standard/quot_print.h
/usr/local/php-5.6.5/include/php/ext/standard/scanf.h
/usr/local/php-5.6.5/include/php/ext/standard/sha1.h
/usr/local/php-5.6.5/include/php/ext/standard/streamsfuncs.h
/usr/local/php-5.6.5/include/php/ext/standard/uniqid.h
/usr/local/php-5.6.5/include/php/ext/standard/url.h
/usr/local/php-5.6.5/include/php/ext/standard/url_scanner_ex.h
/usr/local/php-5.6.5/include/php/ext/standard/winver.h
/usr/local/php-5.6.5/include/php/ext/xml/expat_compat.h
/usr/local/php-5.6.5/include/php/ext/xml/php_xml.h
/usr/local/php-5.6.5/include/php/main/SAPI.h
/usr/local/php-5.6.5/include/php/main/build-defs.h
/usr/local/php-5.6.5/include/php/main/fopen_wrappers.h
/usr/local/php-5.6.5/include/php/main/php.h
/usr/local/php-5.6.5/include/php/main/php_compat.h
/usr/local/php-5.6.5/include/php/main/php_config.h
/usr/local/php-5.6.5/include/php/main/php_content_types.h
/usr/local/php-5.6.5/include/php/main/php_getopt.h
/usr/local/php-5.6.5/include/php/main/php_globals.h
/usr/local/php-5.6.5/include/php/main/php_ini.h
/usr/local/php-5.6.5/include/php/main/php_main.h
/usr/local/php-5.6.5/include/php/main/php_memory_streams.h
/usr/local/php-5.6.5/include/php/main/php_network.h
/usr/local/php-5.6.5/include/php/main/php_open_temporary_file.h
/usr/local/php-5.6.5/include/php/main/php_output.h
/usr/local/php-5.6.5/include/php/main/php_reentrancy.h
/usr/local/php-5.6.5/include/php/main/php_scandir.h
/usr/local/php-5.6.5/include/php/main/php_stdint.h
/usr/local/php-5.6.5/include/php/main/php_streams.h
/usr/local/php-5.6.5/include/php/main/php_syslog.h
/usr/local/php-5.6.5/include/php/main/php_ticks.h
/usr/local/php-5.6.5/include/php/main/php_variables.h
/usr/local/php-5.6.5/include/php/main/php_version.h
/usr/local/php-5.6.5/include/php/main/rfc1867.h
/usr/local/php-5.6.5/include/php/main/snprintf.h
/usr/local/php-5.6.5/include/php/main/spprintf.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_context.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_filter_api.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_glob_wrapper.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_mmap.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_plain_wrapper.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_transport.h
/usr/local/php-5.6.5/include/php/main/streams/php_stream_userspace.h
/usr/local/php-5.6.5/include/php/main/streams/php_streams_int.h
/usr/local/php-5.6.5/include/php/main/win32_internal_function_disabled.h
/usr/local/php-5.6.5/include/php/main/win95nt.h
/usr/local/php-5.6.5/include/php/sapi/cli/cli.h
/usr/local/php-5.6.5/lib/php/.depdb
/usr/local/php-5.6.5/lib/php/.depdblock
/usr/local/php-5.6.5/lib/php/.filemap
/usr/local/php-5.6.5/lib/php/.lock
/usr/local/php-5.6.5/lib/php/Archive/Tar.php
/usr/local/php-5.6.5/lib/php/Console/Getopt.php
/usr/local/php-5.6.5/lib/php/OS/Guess.php
/usr/local/php-5.6.5/lib/php/PEAR.php
/usr/local/php-5.6.5/lib/php/PEAR/Autoloader.php
/usr/local/php-5.6.5/lib/php/PEAR/Builder.php
/usr/local/php-5.6.5/lib/php/PEAR/ChannelFile.php
/usr/local/php-5.6.5/lib/php/PEAR/ChannelFile/Parser.php
/usr/local/php-5.6.5/lib/php/PEAR/Command.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Auth.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Auth.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Build.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Build.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Channels.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Channels.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Common.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Config.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Config.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Install.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Install.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Mirror.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Mirror.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Package.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Package.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Pickle.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Pickle.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Registry.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Registry.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Remote.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Remote.xml
/usr/local/php-5.6.5/lib/php/PEAR/Command/Test.php
/usr/local/php-5.6.5/lib/php/PEAR/Command/Test.xml
/usr/local/php-5.6.5/lib/php/PEAR/Common.php
/usr/local/php-5.6.5/lib/php/PEAR/Config.php
/usr/local/php-5.6.5/lib/php/PEAR/Dependency2.php
/usr/local/php-5.6.5/lib/php/PEAR/DependencyDB.php
/usr/local/php-5.6.5/lib/php/PEAR/Downloader.php
/usr/local/php-5.6.5/lib/php/PEAR/Downloader/Package.php
/usr/local/php-5.6.5/lib/php/PEAR/ErrorStack.php
/usr/local/php-5.6.5/lib/php/PEAR/Exception.php
/usr/local/php-5.6.5/lib/php/PEAR/FixPHP5PEARWarnings.php
/usr/local/php-5.6.5/lib/php/PEAR/Frontend.php
/usr/local/php-5.6.5/lib/php/PEAR/Frontend/CLI.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Cfg.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Cfg.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Common.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Data.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Data.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Doc.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Doc.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Ext.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Ext.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Php.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Php.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Script.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Script.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Src.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Src.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Test.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Test.xml
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Www.php
/usr/local/php-5.6.5/lib/php/PEAR/Installer/Role/Www.xml
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/Generator/v1.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/Generator/v2.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/Parser/v1.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/Parser/v2.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/v1.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/v2.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/v2/Validator.php
/usr/local/php-5.6.5/lib/php/PEAR/PackageFile/v2/rw.php
/usr/local/php-5.6.5/lib/php/PEAR/Packager.php
/usr/local/php-5.6.5/lib/php/PEAR/REST.php
/usr/local/php-5.6.5/lib/php/PEAR/REST/10.php
/usr/local/php-5.6.5/lib/php/PEAR/REST/11.php
/usr/local/php-5.6.5/lib/php/PEAR/REST/13.php
/usr/local/php-5.6.5/lib/php/PEAR/Registry.php
/usr/local/php-5.6.5/lib/php/PEAR/RunTest.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Common.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Postinstallscript.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Postinstallscript/rw.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Replace.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Replace/rw.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Unixeol.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Unixeol/rw.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Windowseol.php
/usr/local/php-5.6.5/lib/php/PEAR/Task/Windowseol/rw.php
/usr/local/php-5.6.5/lib/php/PEAR/Validate.php
/usr/local/php-5.6.5/lib/php/PEAR/Validator/PECL.php
/usr/local/php-5.6.5/lib/php/PEAR/XMLParser.php
/usr/local/php-5.6.5/lib/php/PEAR5.php
/usr/local/php-5.6.5/lib/php/Structures/Graph.php
/usr/local/php-5.6.5/lib/php/Structures/Graph/Manipulator/AcyclicTest.php
/usr/local/php-5.6.5/lib/php/Structures/Graph/Manipulator/TopologicalSorter.php
/usr/local/php-5.6.5/lib/php/Structures/Graph/Node.php
/usr/local/php-5.6.5/lib/php/System.php
/usr/local/php-5.6.5/lib/php/XML/Util.php
/usr/local/php-5.6.5/lib/php/build/Makefile.global
/usr/local/php-5.6.5/lib/php/build/acinclude.m4
/usr/local/php-5.6.5/lib/php/build/config.guess
/usr/local/php-5.6.5/lib/php/build/config.sub
/usr/local/php-5.6.5/lib/php/build/libtool.m4
/usr/local/php-5.6.5/lib/php/build/ltmain.sh
/usr/local/php-5.6.5/lib/php/build/mkdep.awk
/usr/local/php-5.6.5/lib/php/build/phpize.m4
/usr/local/php-5.6.5/lib/php/build/run-tests.php
/usr/local/php-5.6.5/lib/php/build/scan_makefile_in.awk
/usr/local/php-5.6.5/lib/php/build/shtool
/usr/local/php-5.6.5/lib/php/data/PEAR/package.dtd
/usr/local/php-5.6.5/lib/php/data/PEAR/template.spec
/usr/local/php-5.6.5/lib/php/data/Structures_Graph/LICENSE
/usr/local/php-5.6.5/lib/php/extensions/no-debug-zts-20131226/opcache.a
/usr/local/php-5.6.5/lib/php/extensions/no-debug-zts-20131226/opcache.so
/usr/local/php-5.6.5/lib/php/pearcmd.php
/usr/local/php-5.6.5/lib/php/peclcmd.php
/usr/local/php-5.6.5/php/php/fpm/status.html
/usr/local/php-5.6.5/sbin/php-fpm
/usr/local/php-5.6.5/sbin/init.d.php-fpm

%post
sed -i "/init.d.php-fpm/d" /etc/rc.d/rc.local
echo "/usr/local/php-5.6.5/sbin/init.d.php-fpm start" >> /etc/rc.d/rc.local
touch /usr/local/php-5.6.5/var/log/php-errors.log
chown www.www /usr/local/php-5.6.5/var/log/php-errors.log
%preun

%postun
rm -rf /usr/local/php-5.6.5
sed -i "/php/d" /etc/rc.d/rc.local

%doc



%changelog

