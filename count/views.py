from django.shortcuts import redirect, render
from .models import Item, Order
from django.views.decorators.csrf import csrf_protect  # Ensure CSRF protection


@csrf_protect  # Apply CSRF protection decorator
def orders_view(request):
    # Get all items from the database
    items = Item.objects.all()

    # Handle POST request (update item quantities)
    if request.method == "POST":
        for item_id, quantity in request.POST.items():
            if item_id.startswith("item_"):  # Check if it's an item quantity field
                item_pk = int(item_id.split("_")[1])  # Extract item ID
                try:
                    item = Item.objects.get(pk=item_pk)
                    # Update quantity (ensure it doesn't go below 0)
                    item.quantity += int(quantity)
                    item.save()
                except Item.DoesNotExist:
                    pass  # Handle potential errors gracefully
        # Reset form data after successful POST (clears displayed quantities)
        request.session["form_data"] = {}  # Clear form data in session
        return redirect(
            "count:home"
        )  # Redirect to the orders view after successful creation

    # Retrieve form data from session (if present) to pre-populate form
    form_data = request.session.get("form_data", {})
    # Render the template with the list of items
    context = {"items": items, "form_data": form_data}
    return render(request, "count/orders.html", context)


@csrf_protect  # Apply CSRF protection decorator
def new_item_view(request):
    if request.method == "POST":
        new_item_name = request.POST["new_item_name"]
        new_item = Item.objects.create(name=new_item_name)
        return redirect("count:new_item")
        # Consider adding a success message or redirecting to a different page
    return render(request, "count/new_item.html")


def delete_view(request):
    if request.method == "POST":
        # Validate and handle potential errors
        try:
            item_name = request.POST.get("item_name")
            item = Item.objects.get(name=item_name)  # Search by name
        except Item.DoesNotExist:
            return render(
                request,
                "count/delete.html",
                {"error": "Item not found."},
            )

        # Confirmation logic for the found item (similar to the previous approach)
        if "confirm_delete" in request.POST:
            item.delete()
            return redirect("count:delete")
        else:
            return render(request, "count/delete.html", {"item": item})

    return render(request, "count/delete.html")


def order_log(request):
    orders = Order.objects.all().order_by(
        "-created_at"
    )  # Order by creation date descending
    context = {"orders": orders}
    return render(request, "count/order_log.html", context)
