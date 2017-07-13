Name:		nginx
Version:	1.6.2
Release:	1%{?dist}
Summary:	NGINX

Group:		Applications/Internet
License:	GPLv2+
URL:		http://nginx.org/
Source0:	nginx-1.6.2.tar.gz
Source1:    nginx.conf
Source2:    status.conf
Source3:    openssl-1.0.1t.tar.gz

#BuildRequires:	

%description


%prep
%setup -q


%build
./configure \
--prefix=/usr/local/%{name}-%{version} \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_sub_module \
--with-openssl=../openssl-1.0.1t \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--without-select_module \
--without-poll_module \
--without-http_ssi_module \
--without-http_userid_module \
--without-http_geo_module \
--without-http_memcached_module \
--without-http_map_module \
--without-http_scgi_module \
--without-http_uwsgi_module \
--without-mail_pop3_module \
--without-mail_imap_module \
--without-mail_smtp_module \
--without-http_autoindex_module
make %{?_smp_mflags}


%install
%make_install
rm -rf %{buildroot}/usr/local/%{name}-%{version}/html/
mkdir -p %{buildroot}/usr/local/%{name}-%{version}/conf/vhosts
mkdir -p %{buildroot}/usr/local/%{name}-%{version}/logs/
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}/usr/local/%{name}-%{version}/conf/nginx.conf
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}/usr/local/%{name}-%{version}/conf/vhosts/status.conf

%files
%defattr(-,root,root)
/usr/local/nginx-1.6.2/conf/fastcgi.conf
/usr/local/nginx-1.6.2/conf/fastcgi.conf.default
/usr/local/nginx-1.6.2/conf/fastcgi_params
/usr/local/nginx-1.6.2/conf/fastcgi_params.default
/usr/local/nginx-1.6.2/conf/koi-utf
/usr/local/nginx-1.6.2/conf/koi-win
/usr/local/nginx-1.6.2/conf/mime.types
/usr/local/nginx-1.6.2/conf/mime.types.default
/usr/local/nginx-1.6.2/conf/nginx.conf
/usr/local/nginx-1.6.2/conf/nginx.conf.default
/usr/local/nginx-1.6.2/conf/scgi_params
/usr/local/nginx-1.6.2/conf/scgi_params.default
/usr/local/nginx-1.6.2/conf/uwsgi_params
/usr/local/nginx-1.6.2/conf/uwsgi_params.default
/usr/local/nginx-1.6.2/conf/win-utf
/usr/local/nginx-1.6.2/sbin/nginx
/usr/local/nginx-1.6.2/logs
/usr/local/nginx-1.6.2/conf/vhosts

%post
sed -i "/nginx/d" /etc/rc.d/rc.local
sed -i '$a\0 0 * * * root /usr/sbin/logrotate -f /etc/logrotate.d/nginx' /etc/crontab
echo "/usr/local/nginx-1.6.2/sbin/nginx" >> /etc/rc.local
/usr/local/nginx-1.6.2/sbin/nginx
cat > /etc/logrotate.d/nginx <<'EOF'
/home/logs/*.log {
   daily
   dateext
   maxage 7
   rotate 7
   missingok
   notifempty
   sharedscripts
   postrotate
       /bin/kill -USR1 `cat /usr/local/nginx-1.6.2/logs/nginx.pid`
   endscript
}
EOF

%preun

%postun
rm -rf /usr/local/nginx-1.6.2
sed -i "/nginx/d" /etc/rc.d/rc.local
sed -i "/nginx/d" /etc/crontab

%doc

%changelog

