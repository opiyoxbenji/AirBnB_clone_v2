class web_static {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/data/web_static':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
    require => File['/data/web_static'],
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => template('web_static/index.html'),
    require => File['/data/web_static/releases/test'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('web_static/nginx.conf.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

