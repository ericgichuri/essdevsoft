import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask_mail import Mail,Message
from email_validator import validate_email, EmailNotValidError

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, 
            template_folder=os.path.join(basedir, '../templates'),
            static_folder=os.path.join(basedir, '../static'))

app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = (
    "ESS DEVSOFT",
    os.getenv("MAIL_USERNAME")
)


mail = Mail(app)

PROJECTS = [

    {
        "code": "PRO001",
        "title": "MRENT Kenya",
        "slug": "mrent-kenya",
        "short_description": "A real estate marketplace connecting Kenyan landlords and tenants.",
        "description": "MRENTKENYA is your trusted rental platform, connecting property owners with potential tenants across Kenya. We simplify the rental journey through a secure, user-friendly platform built for today's housing needs.",
        "image": "images/projects/mrentkenya/mrentkenya.svg",
        "gallery": [
            "images/projects/mrentkenya/mrentkenya1.png",
            "images/projects/mrentkenya/mrentkenya2.png",
            "images/projects/mrentkenya/mrentkenya3.png",
            "images/projects/mrentkenya/mrentkenya4.png"
        ],
        "category": "Web Application",
        "client": "MRENT Kenya",
        "year": 2026,
        "status": "Completed",
        "featured": True,
        "technologies": [
            "PHP",
            "Tailwind CSS",
            "MySQL",
            "JavaScript"
        ],
        "features": [
            "Property Listing",
            "Landloard Portal",
            "Property Boost",
            "Admin Dashboard",
            "Reports"
        ],
        "project_url": "https://mrentkenya.co.ke",
        "github": None
    },

    {
        "code": "PRO002",
        "title": "ESS POS",
        "slug": "ess-pos",
        "short_description": "A complete Point of Sale solution for retail businesses.",
        "description": "ESS POS simplifies retail operations through sales management, inventory tracking, customer management and reporting.",
        "image": "images/projects/esspos/esspos.svg",
        "gallery": [
            "images/projects/esspos/esspos1.png",
            "images/projects/esspos/esspos2.png",
            "images/projects/esspos/esspos3.png",
            "images/projects/esspos/esspos4.png",
        ],
        "category": "Business Software",
        "client": "Private",
        "year": 2026,
        "status": "Completed",
        "featured": True,
        "technologies": [
            "Python",
            "Flask",
            "MySQL",
            "Tailwind",
            "JavaScript"
        ],
        "features": [
            "Sales",
            "Inventory",
            "Receipts",
            "Reports",
            "User Roles",
            "Suppliers Invoice",
            "Mpesa Integration"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO003",
        "title": "ESS EduSystem",
        "slug": "ess-edusystem",
        "short_description": "School management platform for administrators, teachers and students.",
        "description": "A comprehensive, high-performance desktop and web ecosystem designed for Kenyan schools. From automated financial auditing to streamlined student admissions, we bridge the gap between complex school administration and digital efficiency.",
        "image": "images/projects/essedusystem/essedusystem.png",
        "gallery": [
            "images/projects/essedusystem/academics.png",
            "images/projects/essedusystem/library.png",
            "images/projects/essedusystem/student.png",
            "images/projects/essedusystem/finance.png"
            ],
        "category": "Education System",
        "client": "Private",
        "year": 2026,
        "status": "Completed",
        "featured": True,
        "technologies": [
            "Python",
            "Flask",
            "MySQL",
            "Tailwind CSS"
        ],
        "features": [
            "Admissions",
            "Attendance",
            "Exam Results",
            "Fees",
            "Parent Portal",
            "Library & Circulation",
            "Role Based Access",
            "Accountability Audit"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO004",
        "title": "FleetRent",
        "slug": "fleetrent",
        "short_description": "Fleet and vehicle rental management platform.",
        "description": "FleetRent provides businesses with vehicle booking, maintenance scheduling, fleet monitoring and rental management.",
        "image": "images/projects/fleetrent/fleetrent.png",
        "gallery": [],
        "category": "Fleet Management",
        "client": "Demo Project",
        "year": 2026,
        "status": "Completed",
        "featured": True,
        "technologies": [
            "PHP",
            "MySQL",
            "Tailwind CSS",
            "JavaScript"
        ],
        "features": [
            "Vehicle Booking",
            "Hire Reports",
            "Maintenance"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO005",
        "title": "Kenya Geo API",
        "slug": "kenya-geo-api",
        "short_description": "REST API providing Kenya administrative location data.",
        "description": "A free API providing counties, sub-counties, wards and other geographical data for Kenya.",
        "image": "images/projects/kenyageoapi/geoapi.svg",
        "gallery": [],
        "category": "REST API",
        "client": "Open Source",
        "year": 2026,
        "status": "Live",
        "featured": True,
        "technologies": [
            "Python",
            "Flask",
            "REST API",
            "JSON"
        ],
        "features": [
            "County Data",
            "Ward Data",
            "REST Endpoints",
            "Fast Responses"
        ],
        "project_url": "https://kenya-geo-api.vercel.app",
        "github": None
    },

    {
        "code": "PRO006",
        "title": "BomaConnect",
        "slug": "bomaconnect",
        "short_description": "A Real estate marktplace and landlord management platform.",
        "description": "A Real estate marktplace. Landlord can post their rentals, manage rentals and collect rent via the platform. Can generate Receipts, Track down vacant rooms.",
        "image": "images/projects/bomaconnect/BomaConnect2V2.svg",
        "gallery": [],
        "category": "Web Application",
        "client": "Personal Project",
        "year": 2026,
        "status": "Completed",
        "featured": True,
        "technologies": [
            "Flask",
            "Tailwind",
            "JS",
            "API"
        ],
        "features": [
            "Subscription",
            "Promotions",
            "Whitelist",
            "Fast Performance"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO007",
        "title": "Church Management System",
        "slug": "church-management-system",
        "short_description": "Software for managing member records, tithes, and event scheduling.",
        "description": "Church MIS is a Desktop software for managing member records, tithes, and event scheduling. Built with a focus on data privacy and ease of use.",
        "image": "images/projects/churchmis/church.png",
        "gallery": [],
        "category": "Management System",
        "client": "Private",
        "year": 2023,
        "status": "Completed",
        "featured": False,
        "technologies": [
            "Python",
            "Custom Tkinter",
            "SQLite"
        ],
        "features": [
            "Reports",
            "Dashboard",
            "Authentication"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO008",
        "title": "E-Commerce Website",
        "slug": "ecommerce-website",
        "short_description": "A full-featured online store with product filtering, secure checkout",
        "description": "A modern E-Commerce Website is responsive full-featured online store with product filtering, secure checkout, and an admin dashboard for inventory and order management.",
        "image": "images/projects/ecommerce/ecommerce.jpeg",
        "gallery": [],
        "category": "Corporate Website",
        "client": "ESS DEVSOFT",
        "year": 2026,
        "status": "Live",
        "featured": False,
        "technologies": [
            "Python",
            "Flask",
            "Tailwind CSS",
            "JavaScript"
        ],
        "features": [
            "Portfolio",
            "Responsive Design",
            "Dark Mode",
            "Project Showcase"
        ],
        "project_url": None,
        "github": None
    },

    {
        "code": "PRO009",
        "title": "Real Estate Website",
        "slug": "real-estate-website",
        "short_description": "A website for property marketplace for buying and selling land and houses.",
        "description": "A robust property marketplace for buying and selling land and houses. Features include advanced location-based search and filtering, a real-time inquiry and notification system, and an integrated blog for market insights.",
        "image": "images/projects/realestate/realestate.png",
        "gallery": [
            "images/projects/realestate/realestate1.png",
            "images/projects/realestate/realestate2.png",
            "images/projects/realestate/realestate3.png",
            "images/projects/realestate/realestate4.png",
            "images/projects/realestate/realestate5.png"
        ],
        "category": "Corporate Website",
        "client": "Private",
        "year": 2026,
        "status": "Published",
        "featured": False,
        "technologies": [
            "PHP",
            "Bootstrap",
            "GitHub"
        ],
        "features": [
            "Admin Dashboard",
            "filter & Search",
            "Blog",
            "Real-time inquiry and notification"
        ],
        "project_url": "",
        "github": "https://github.com/"
    }

]

@app.route("/")
def index():

    featured = [p for p in PROJECTS if p["featured"]][:6]

    return render_template(
        "index.html",
        projects=featured
    )

@app.route("/projects")
def projects():

    return render_template(
        "projects.html",
        projects=PROJECTS
    )

@app.route("/project/<project_code>")
def view_project(project_code):

    project = next(
        (p for p in PROJECTS if p["code"] == project_code),
        None
    )

    if project is None:
        abort(404)

    return render_template(
        "view_project.html",
        project=project
    )

@app.route("/services")
def services():

    return render_template(
        "services.html"
    )

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )

@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


@app.route("/api/send-message", methods=["POST"])
def send_message():
    try:
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            return jsonify({
                "success": False,
                "message": "Name is required."
            })

        if not email:
            return jsonify({
                "success": False,
                "message": "Email is required."
            })

        try:
            validate_email(email)

        except EmailNotValidError:

            return jsonify({
                "success": False,
                "message": "Please enter a valid email address."
            })

        if not subject:
            return jsonify({
                "success": False,
                "message": "Subject is required."
            })

        if not message:

            return jsonify({
                "success": False,
                "message": "Message is required."
            })

        email_message = Message(
            subject=f"Website Contact: {subject}",
            recipients=["essdevsoft@gmail.com"]
        )

        email_message.html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
            </head>

            <body style="margin:0;padding:40px;background:#f4f6f9;font-family:Arial, Helvetica, sans-serif;
            ">
            <table align="center" width="650" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;border:1px solid #e5e7eb;">
                <tr>
                    <td style="background:#1a365d;padding:30px;text-align:center;">
                        <h1 style="margin:0;color:#ffffff;font-size:30px;">
                            ESS DEVSOFT
                        </h1>
                        <p style="margin-top:10px;color:#dbeafe;font-size:15px;">
                            New Contact Form Submission
                        </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:35px;">
                        <h2 style="margin-top:0;color:#1a365d;">
                            Hello Eric,
                        </h2>
                        <p style="color:#475569;line-height:1.8;font-size:15px;">
                            A visitor has submitted the contact form from your website.
                            Below are the details.
                        </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0 35px 35px;">
                        <table width="100%" cellpadding="14" cellspacing="0" style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;">
                            <tr style="background:#f8fafc;">
                                <td width="180"><strong>Name</strong></td>
                                <td>{name}</td>
                            </tr>
                            <tr>
                                <td><strong>Email</strong></td>
                                <td>
                                    <a href="mailto:{email}" style="color:#f97316;text-decoration:none;">
                                        {email}
                                    </a>
                                </td>
                            </tr>
                            <tr style="background:#f8fafc;">
                                <td><strong>Subject</strong></td>
                                <td>{subject}</td>
                            </tr>
                            <tr>
                                <td valign="top"><strong>Message</strong></td>
                                <td style="line-height:1.8;white-space:pre-wrap;">
                                    {message}
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="background:#f8fafc;padding:25px;text-align:center;border-top:1px solid #e5e7eb;">
                        <p style="margin:0;color:#64748b;font-size:13px;">
                            This message was sent from the
                            <strong>ESS DEVSOFT</strong> website contact form.
                        </p>
                    </td>
                </tr>
            </table>
            </body>
            </html>
            """

        mail.send(email_message)

        return jsonify({
            "success": True,
            "message": "Your message has been sent successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })

if __name__=="__main__":
    app.run(debug=True)