from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from health_check.views import MainView


class HealthCheckCustomView(MainView):
    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        status_code = 500 if self.errors else 200

        return JsonResponse(
            {
                str(p.identifier()): {
                    "status": str(p.pretty_status()),
                    "time_taken": str(p.time_taken),
                }
                for p in self.plugins
            },
            status=status_code,
        )
