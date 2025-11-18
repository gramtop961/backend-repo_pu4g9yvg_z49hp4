"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class Inquiry(BaseModel):
    """
    Restaurant partner inquiries/leads
    Collection name: "inquiry"
    """
    restaurant_name: str = Field(..., description="Restaurant name")
    contact_name: str = Field(..., description="Primary contact person")
    phone: str = Field(..., description="Contact phone number")
    email: Optional[EmailStr] = Field(None, description="Contact email")
    city: Optional[str] = Field(None, description="City/Location")
    platform: Optional[Literal['Zomato','Swiggy','Both','Other']] = Field('Both', description="Target platform")
    shoot_type: Optional[str] = Field(None, description="Type of shoot: Menu, Ambience, Team, Video")
    budget_range: Optional[str] = Field(None, description="Estimated budget range")
    heard_from: Optional[str] = Field(None, description="How they heard about us")
    message: Optional[str] = Field(None, description="Additional details")
    status: Literal['new','contacted','quoted','won','lost'] = Field('new', description="Lead status")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
