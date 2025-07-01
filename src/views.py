from django.shortcuts import redirect

from django.views.generic import TemplateView

from products.models import Product
from src.parser import extract_data


class ShowMainPage(TemplateView):
    template_name = "src/index.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            data = request.POST.get("data")
            request.session["saved_data"] = data
            return redirect("src:result")
        return super().get(request, *args, **kwargs)


class ShowResult(TemplateView):
    template_name = "src/result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saved_data"] = self.request.session.get("saved_data")
        element = self.request.session.get("saved_data")
        parser_data = extract_data(element)
        context["parser_data"] = parser_data

        for item in parser_data:
            new_object = Product(
                title=item[0],
                price=int(item[2]),
                discounted_price=int(item[1]),
                rating=float(item[3]),
                reviews=int(item[4]),
            )
            new_object.save()

        return context
