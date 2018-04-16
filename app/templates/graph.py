{% extends "base.html" %} 
 
 
{% block footer %} 
{{ super() }} 
{% endblock %} 

 
{% block extrahead %} 
    <link href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.1/nv.d3.min.css" rel="stylesheet" /> 
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script> 
    <script src="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.7.1/nv.d3.min.js"></script> 
{% endblock %} 


{%- block body %} 
  {{ super() }} 

 
{%- endblock %} 
