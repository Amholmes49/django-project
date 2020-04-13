# Rental Hub
This site is designed to track and manage properties and tenants.  Tenants and properties can be added, edited, viewed, and deleted.  A tenant or multiple tenants can be associated with each property.  To create, edit, delete, and view tenants the user be logged in. To create, edit, and delete properties the user must be logged in.  Anyone can view available properties.


## Project Links
* https://github.com/Amholmes49/django-project
* https://rental-hub.herokuapp.com/


### MVP/PostMVP
The MVP includes two non-user models, CRUD for tenants, and required authentication for creating, deleting, and editing properties and tenants. 

#### MVP Example
- https://rental-hub.herokuapp.com/
- authentication
- CRUD

## Code Snippet
``
<h3>Tenants</h3>
    <ul>
    {% for tenant in property.tenants.all %}

    <li>
        <a href="">{{ tenant.full_name }}</a>
  
    </li>
    {% endfor %}
</ul> 

## Additional Libraries
* phone_field

## Issues and Resoltions
    Initially had foreign key set to protect as I didn't want a property delete to include the tenants as well.  I wanted the application to notify a user to remove the tenants from the property first.  I was unable to get this working.

### Future Enhancements/Recomendations
* Have Active Properties and Active Tenants vs showing all tenants and properties.  Tenants would be based of lease dates.


### Prerequisites
  * django
  * python
  * phone libraries

