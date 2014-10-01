# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf import settings
from django.conf.urls import handler404, include, patterns
from django.contrib import admin

from funfactory.monkeypatches import patch


patch()
admin.autodiscover()

# The default django 500 handler doesn't run the ContextProcessors, which breaks
# the base template page. So we replace it with one that does!
handler500 = 'lib.bedrock_util.server_error_view'


urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    # Main pages
    (r'^lightbeam/', include('bedrock.lightbeam.urls')),
    (r'^foundation/', include('bedrock.foundation.urls')),
    (r'^gigabit/', include('bedrock.gigabit.urls')),
    (r'^grants/', include('bedrock.grants.urls')),
    (r'^about/legal/', include('bedrock.legal.urls')),
    (r'^persona/', include('bedrock.persona.urls')),
    (r'^press/', include('bedrock.press.urls')),
    (r'^privacy', include('bedrock.privacy.urls')),
    (r'^styleguide/', include('bedrock.styleguide.urls')),
    (r'^tabzilla/', include('bedrock.tabzilla.urls')),
    (r'^security/', include('bedrock.security.urls')),
    (r'', include('bedrock.firefox.urls')),
    (r'', include('bedrock.mozorg.urls')),
    (r'', include('bedrock.newsletter.urls')),
    (r'', include('bedrock.redirects.urls')),
    (r'', include('bedrock.research.urls')),
    (r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
     {'document_root': settings.ROOT}),

    # L10n example.
    (r'^l10n_example/',
     include('bedrock.l10n_example.urls')),

    # Facebook Apps
    (r'^facebookapps/',
     include('bedrock.facebookapps.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns(
        '',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
        (r'^404/$', handler404),
        (r'^500/$', handler500))
