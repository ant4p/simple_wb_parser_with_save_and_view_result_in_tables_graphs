from django_filters.views import FilterView


from products.filters import ProductFitlter
from products.models import Product


class ProductsListView(FilterView):
    model = Product
    template_name = "products/products.html"
    filterset_class = ProductFitlter
    context_object_name = "products_list"

    def get_context_data(self, **kwargs):
        import plotly.graph_objects as go

        context = super().get_context_data(**kwargs)
        # queryset = self.get_queryset()

        filtered_queryset = self.filterset.qs

        if filtered_queryset.exists():
            titles = [item.title for item in filtered_queryset]
            prices = [item.price for item in filtered_queryset]

            fig = go.Figure(data=[go.Bar(x=titles, y=prices)])
            fig.update_layout(
                title="Гистограма распределения 'Цены' и 'Количества товара'",
                xaxis_title="Название товара",
                yaxis_title="Цена",
            )
            context["plot_div_histogram"] = fig.to_html(
                full_html=False, default_height=300
            )
        else:
            context["plot_div_histogram"] = None

        if filtered_queryset.exists():
            discount = [
                int(((item.price - item.discounted_price) / item.price * 100))
                for item in filtered_queryset
            ]
            rating = [item.rating for item in filtered_queryset]

            line_trace = go.Scatter(
                x=rating, y=discount, mode="markers", name="Линейная диаграма"
            )

            fig = go.Figure(data=[line_trace])
            fig.update_layout(
                title="График линейный - влияние 'Размера скидки' на 'Рейтинг товара'",
                xaxis_title="Рейтинг",
                yaxis_title="Размер скидки",
            )
            context["plot_div_line"] = fig.to_html(full_html=False, default_height=300)
        else:
            context["plot_div_line"] = None

        return context
