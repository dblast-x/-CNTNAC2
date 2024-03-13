from django.shortcuts import render
from .models import Item
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
                    item.quantity = max(int(quantity), 0)
                    item.save()
                except Item.DoesNotExist:
                    pass  # Handle potential errors gracefully

    # Render the template with the list of items
    context = {"items": items}
    return render(request, "count/orders.html", context)


@csrf_protect  # Apply CSRF protection decorator
def new_item_view(request):
    if request.method == "POST":
        new_item_name = request.POST["new_item_name"]
        new_item = Item.objects.create(name=new_item_name)
        # Consider adding a success message or redirecting to a different page
    context = {}  # Empty context for now
    return render(request, "count/new_item.html", context)
