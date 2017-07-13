Name:		libmemcached
Version:	1.0.18
Release:	1%{?dist}
Summary:	LIBMEMCACHED

Group:		Applications/Internet
License:	GPLv2+
URL:		http://libmemcached.org/
Source0:	libmemcached-1.0.18.tar.gz

#BuildRequires:	
#Requires:	

%description


%prep
%setup -q


%build
%configure
./configure \
--prefix=/usr/local/%{name} \
--disable-sasl
make %{?_smp_mflags}


%install
%make_install
rm -rf %{buildroot}/usr/local/%{name}/share

%files
/usr/local/libmemcached/bin/memcapable
/usr/local/libmemcached/bin/memcat
/usr/local/libmemcached/bin/memcp
/usr/local/libmemcached/bin/memdump
/usr/local/libmemcached/bin/memerror
/usr/local/libmemcached/bin/memexist
/usr/local/libmemcached/bin/memflush
/usr/local/libmemcached/bin/memparse
/usr/local/libmemcached/bin/memping
/usr/local/libmemcached/bin/memrm
/usr/local/libmemcached/bin/memslap
/usr/local/libmemcached/bin/memstat
/usr/local/libmemcached/bin/memtouch
/usr/local/libmemcached/include/libhashkit-1.0/algorithm.h
/usr/local/libmemcached/include/libhashkit-1.0/behavior.h
/usr/local/libmemcached/include/libhashkit-1.0/configure.h
/usr/local/libmemcached/include/libhashkit-1.0/digest.h
/usr/local/libmemcached/include/libhashkit-1.0/function.h
/usr/local/libmemcached/include/libhashkit-1.0/has.h
/usr/local/libmemcached/include/libhashkit-1.0/hashkit.h
/usr/local/libmemcached/include/libhashkit-1.0/hashkit.hpp
/usr/local/libmemcached/include/libhashkit-1.0/str_algorithm.h
/usr/local/libmemcached/include/libhashkit-1.0/strerror.h
/usr/local/libmemcached/include/libhashkit-1.0/string.h
/usr/local/libmemcached/include/libhashkit-1.0/types.h
/usr/local/libmemcached/include/libhashkit-1.0/visibility.h
/usr/local/libmemcached/include/libhashkit/hashkit.h
/usr/local/libmemcached/include/libmemcached-1.0/alloc.h
/usr/local/libmemcached/include/libmemcached-1.0/allocators.h
/usr/local/libmemcached/include/libmemcached-1.0/analyze.h
/usr/local/libmemcached/include/libmemcached-1.0/auto.h
/usr/local/libmemcached/include/libmemcached-1.0/basic_string.h
/usr/local/libmemcached/include/libmemcached-1.0/behavior.h
/usr/local/libmemcached/include/libmemcached-1.0/callback.h
/usr/local/libmemcached/include/libmemcached-1.0/callbacks.h
/usr/local/libmemcached/include/libmemcached-1.0/configure.h
/usr/local/libmemcached/include/libmemcached-1.0/defaults.h
/usr/local/libmemcached/include/libmemcached-1.0/delete.h
/usr/local/libmemcached/include/libmemcached-1.0/deprecated_types.h
/usr/local/libmemcached/include/libmemcached-1.0/dump.h
/usr/local/libmemcached/include/libmemcached-1.0/encoding_key.h
/usr/local/libmemcached/include/libmemcached-1.0/error.h
/usr/local/libmemcached/include/libmemcached-1.0/exception.hpp
/usr/local/libmemcached/include/libmemcached-1.0/exist.h
/usr/local/libmemcached/include/libmemcached-1.0/fetch.h
/usr/local/libmemcached/include/libmemcached-1.0/flush.h
/usr/local/libmemcached/include/libmemcached-1.0/flush_buffers.h
/usr/local/libmemcached/include/libmemcached-1.0/get.h
/usr/local/libmemcached/include/libmemcached-1.0/hash.h
/usr/local/libmemcached/include/libmemcached-1.0/limits.h
/usr/local/libmemcached/include/libmemcached-1.0/memcached.h
/usr/local/libmemcached/include/libmemcached-1.0/memcached.hpp
/usr/local/libmemcached/include/libmemcached-1.0/options.h
/usr/local/libmemcached/include/libmemcached-1.0/parse.h
/usr/local/libmemcached/include/libmemcached-1.0/platform.h
/usr/local/libmemcached/include/libmemcached-1.0/quit.h
/usr/local/libmemcached/include/libmemcached-1.0/result.h
/usr/local/libmemcached/include/libmemcached-1.0/return.h
/usr/local/libmemcached/include/libmemcached-1.0/sasl.h
/usr/local/libmemcached/include/libmemcached-1.0/server.h
/usr/local/libmemcached/include/libmemcached-1.0/server_list.h
/usr/local/libmemcached/include/libmemcached-1.0/stats.h
/usr/local/libmemcached/include/libmemcached-1.0/storage.h
/usr/local/libmemcached/include/libmemcached-1.0/strerror.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/allocator.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/analysis.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/callback.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/memcached.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/result.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/sasl.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/server.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/stat.h
/usr/local/libmemcached/include/libmemcached-1.0/struct/string.h
/usr/local/libmemcached/include/libmemcached-1.0/touch.h
/usr/local/libmemcached/include/libmemcached-1.0/triggers.h
/usr/local/libmemcached/include/libmemcached-1.0/types.h
/usr/local/libmemcached/include/libmemcached-1.0/types/behavior.h
/usr/local/libmemcached/include/libmemcached-1.0/types/callback.h
/usr/local/libmemcached/include/libmemcached-1.0/types/connection.h
/usr/local/libmemcached/include/libmemcached-1.0/types/hash.h
/usr/local/libmemcached/include/libmemcached-1.0/types/return.h
/usr/local/libmemcached/include/libmemcached-1.0/types/server_distribution.h
/usr/local/libmemcached/include/libmemcached-1.0/verbosity.h
/usr/local/libmemcached/include/libmemcached-1.0/version.h
/usr/local/libmemcached/include/libmemcached-1.0/visibility.h
/usr/local/libmemcached/include/libmemcached/memcached.h
/usr/local/libmemcached/include/libmemcached/memcached.hpp
/usr/local/libmemcached/include/libmemcached/util.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/flush.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/ostream.hpp
/usr/local/libmemcached/include/libmemcachedutil-1.0/pid.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/ping.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/pool.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/util.h
/usr/local/libmemcached/include/libmemcachedutil-1.0/version.h
/usr/local/libmemcached/lib/libhashkit.a
/usr/local/libmemcached/lib/libhashkit.la
/usr/local/libmemcached/lib/libhashkit.so
/usr/local/libmemcached/lib/libhashkit.so.2
/usr/local/libmemcached/lib/libhashkit.so.2.0.0
/usr/local/libmemcached/lib/libmemcached.a
/usr/local/libmemcached/lib/libmemcached.la
/usr/local/libmemcached/lib/libmemcached.so
/usr/local/libmemcached/lib/libmemcached.so.11
/usr/local/libmemcached/lib/libmemcached.so.11.0.0
/usr/local/libmemcached/lib/libmemcachedutil.a
/usr/local/libmemcached/lib/libmemcachedutil.la
/usr/local/libmemcached/lib/libmemcachedutil.so
/usr/local/libmemcached/lib/libmemcachedutil.so.2
/usr/local/libmemcached/lib/libmemcachedutil.so.2.0.0
/usr/local/libmemcached/lib/pkgconfig/libmemcached.pc
%doc



%changelog

