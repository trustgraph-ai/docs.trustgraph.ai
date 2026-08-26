import random
import re
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL, XSD

def make_uri_name(text: str) -> str:
    """Sanitizes text to create clean URI fragments."""
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return ''.join(word.capitalize() for word in cleaned.split())

def to_channel_name(text: str) -> str:
    """Formats a string into a Slack channel handle format."""
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return '#' + '-'.join(cleaned.split())

def build_annotated_onboarding_graph() -> Graph:
    random.seed(42)
    
    g = Graph()
    EX = Namespace("http://example.org/ontology/office#")
    
    # Bind prefixes for human-readable Turtle output
    g.bind("", EX)
    g.bind("owl", OWL)
    g.bind("rdfs", RDFS)
    g.bind("xsd", XSD)

    # =========================================================================
    # 1. ONTOLOGY DEFINITION (Classes, Object Properties, Data Properties)
    # =========================================================================
    
    ontology_uri = URIRef("http://example.org/ontology/office")
    g.add((ontology_uri, RDF.type, OWL.Ontology))
    g.add((ontology_uri, RDFS.label, Literal("Office Onboarding and Service Ownership Ontology")))
    g.add((ontology_uri, RDFS.comment, Literal("Defines organizational structure, service ownership, access rules, and approval workflows.")))

    # Classes
    classes = {
        "Person": ("Person", "An individual employee, contractor, or team member within the organization."),
        "Role": ("Role", "A designated job function, title, or position held by a Person."),
        "Team": ("Team", "A functional group of individuals collaborating on specific operational goals."),
        "Department": ("Department", "A top-level organizational unit containing multiple teams."),
        "Service": ("Service", "An internal tool, software platform, infrastructure system, or SaaS application."),
        "Process": ("Process", "A structured sequence of administrative steps or workflows."),
        "ApprovalStep": ("Approval Step", "A specific phase within a Process where sign-off is required."),
        "Channel": ("Channel", "A communication medium, such as a Slack channel or distribution list.")
    }

    for class_name, (label, comment) in classes.items():
        c_uri = EX[class_name]
        g.add((c_uri, RDF.type, OWL.Class))
        g.add((c_uri, RDFS.label, Literal(label)))
        g.add((c_uri, RDFS.comment, Literal(comment)))

    # Object Properties
    obj_properties = {
        "hasRole": ("has role", "Links a Person to their assigned official Role or job title.", EX.Person, EX.Role),
        "memberOf": ("member of", "Associates a Person with the Team they belong to.", EX.Person, EX.Team),
        "owns": ("owns", "Indicates that a specific Team is responsible for maintaining and supporting a Service.", EX.Team, EX.Service),
        "requiresAccess": ("requires access to", "Specifies that a Role requires default access to a Service to perform duties.", EX.Role, EX.Service),
        "hasStep": ("has step", "Connects an overall Process workflow to an individual ApprovalStep.", EX.Process, EX.ApprovalStep),
        "approvedBy": ("approved by", "Identifies the designated Role authorized to evaluate and sign off on an ApprovalStep.", EX.ApprovalStep, EX.Role),
        "managedBy": ("managed by", "Designates the Person responsible for leading or managing a Team.", EX.Team, EX.Person),
        "belongsToDepartment": ("belongs to department", "Links a Team to its parent Department within corporate structure.", EX.Team, EX.Department),
        "associatedChannel": ("associated channel", "Links an entity (Team, Service, Process) to its primary communication Channel.", None, EX.Channel)
    }

    for prop_name, (label, comment, domain, range_type) in obj_properties.items():
        p_uri = EX[prop_name]
        g.add((p_uri, RDF.type, OWL.ObjectProperty))
        g.add((p_uri, RDFS.label, Literal(label)))
        g.add((p_uri, RDFS.comment, Literal(comment)))
        if domain:
            g.add((p_uri, RDFS.domain, domain))
        if range_type:
            g.add((p_uri, RDFS.range, range_type))

    # Datatype Properties
    g.add((EX.spendLimit, RDF.type, OWL.DatatypeProperty))
    g.add((EX.spendLimit, RDFS.label, Literal("spend limit")))
    g.add((EX.spendLimit, RDFS.comment, Literal("The maximum financial monetary value authorized at this ApprovalStep.")))
    g.add((EX.spendLimit, RDFS.domain, EX.ApprovalStep))
    g.add((EX.spendLimit, RDFS.range, XSD.decimal))

    # =========================================================================
    # 2. INSTANCE DATA GENERATION
    # =========================================================================

    dept_structure = {
        "Engineering": ["Platform Infrastructure", "Core Frontend", "Security Operations"],
        "Human Resources": ["Talent Acquisition", "People Experience"],
        "Finance": ["Corporate Accounting", "Procurement"],
        "Product": ["Product Management", "UX Research"],
        "Operations": ["IT Support Services", "Workplace Operations"]
    }

    team_roles = {
        "Platform Infrastructure": ["DevOps Engineer", "Cloud Architect", "Site Reliability Engineer"],
        "Core Frontend": ["Frontend Developer", "UI Lead"],
        "Security Operations": ["Security Engineer", "AppSec Specialist"],
        "Talent Acquisition": ["Technical Recruiter", "Sourcing Specialist"],
        "People Experience": ["HR Partner", "Onboarding Lead"],
        "Corporate Accounting": ["Financial Accountant", "Staff Accountant"],
        "Procurement": ["Procurement Specialist", "Vendor Manager"],
        "Product Management": ["Product Manager", "Technical PM"],
        "UX Research": ["UX Designer", "Design Researcher"],
        "IT Support Services": ["IT Support Specialist", "System Administrator"],
        "Workplace Operations": ["Facilities Manager", "Office Admin"]
    }

    all_roles = sorted({role for roles in team_roles.values() for role in roles})

    services_list = [
        "GitHub Enterprise", "Jira Software", "AWS Infrastructure",
        "Datadog Monitoring", "Figma Design", "Workday HRIS",
        "QuickBooks Online", "Confluence Wiki", "Okta Identity",
        "Zoom Workplace", "PagerDuty Incident Response", "Coupa Spend Platform"
    ]

    # Departments
    dept_uris = {}
    for dept_name in dept_structure.keys():
        d_uri = EX[f"Dept_{make_uri_name(dept_name)}"]
        dept_uris[dept_name] = d_uri
        g.add((d_uri, RDF.type, EX.Department))
        g.add((d_uri, RDFS.label, Literal(dept_name)))
        g.add((d_uri, RDFS.comment, Literal(f"The {dept_name} organizational department.")))

    # Roles
    role_uris = {}
    for role_name in all_roles:
        r_uri = EX[f"Role_{make_uri_name(role_name)}"]
        role_uris[role_name] = r_uri
        g.add((r_uri, RDF.type, EX.Role))
        g.add((r_uri, RDFS.label, Literal(role_name)))
        g.add((r_uri, RDFS.comment, Literal(f"Job title and governance role of {role_name}.")))

    # Services & Service Channels
    service_uris = []
    for svc in services_list:
        s_uri = EX[f"Svc_{make_uri_name(svc)}"]
        chan_uri = EX[f"Chan_Svc_{make_uri_name(svc)}"]
        chan_name = to_channel_name(f"svc {svc}")
        service_uris.append(s_uri)

        g.add((chan_uri, RDF.type, EX.Channel))
        g.add((chan_uri, RDFS.label, Literal(chan_name)))
        g.add((chan_uri, RDFS.comment, Literal(f"Dedicated communication channel for support and alerts on {svc}.")))

        g.add((s_uri, RDF.type, EX.Service))
        g.add((s_uri, RDFS.label, Literal(svc)))
        g.add((s_uri, RDFS.comment, Literal(f"Internal software service or platform: {svc}.")))
        g.add((s_uri, EX.associatedChannel, chan_uri))

    # Role Access Requirements
    for role_name, r_uri in role_uris.items():
        req_svcs = random.sample(service_uris, random.randint(1, 3))
        for s_uri in req_svcs:
            g.add((r_uri, EX.requiresAccess, s_uri))

    # Teams, Team Channels, and Service Ownership
    team_uris = []
    for dept_name, teams in dept_structure.items():
        d_uri = dept_uris[dept_name]
        for t_name in teams:
            t_uri = EX[f"Team_{make_uri_name(t_name)}"]
            team_uris.append(t_uri)

            chan_uri = EX[f"Chan_Team_{make_uri_name(t_name)}"]
            chan_name = to_channel_name(f"team {t_name}")

            g.add((chan_uri, RDF.type, EX.Channel))
            g.add((chan_uri, RDFS.label, Literal(chan_name)))
            g.add((chan_uri, RDFS.comment, Literal(f"Slack channel for discussions within the {t_name} team.")))

            g.add((t_uri, RDF.type, EX.Team))
            g.add((t_uri, RDFS.label, Literal(f"{t_name} Team")))
            g.add((t_uri, RDFS.comment, Literal(f"Functional team operating under the {dept_name} department.")))
            g.add((t_uri, EX.belongsToDepartment, d_uri))
            g.add((t_uri, EX.associatedChannel, chan_uri))

            owned_svcs = random.sample(service_uris, random.randint(1, 2))
            for s_uri in owned_svcs:
                g.add((t_uri, EX.owns, s_uri))

    # People & Assignments
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Riley",
                   "Avery", "Dakota", "Cameron", "Reese", "Skyler", "Casey", "Jamie",
                   "Peyton", "Quinn", "Logan", "Kendall", "Harper", "Rowan", "Hayden"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
                  "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
                  "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]

    unique_names = list({f"{fn} {ln}" for fn in first_names for ln in last_names})
    random.shuffle(unique_names)
    selected_people = unique_names[:40]

    team_members_map = {t_uri: [] for t_uri in team_uris}

    for idx, name in enumerate(selected_people):
        p_uri = EX[f"Person_{make_uri_name(name)}"]
        t_uri = team_uris[idx % len(team_uris)]
        team_members_map[t_uri].append(p_uri)

        t_name = next(tn for tn_list in dept_structure.values() for tn in tn_list if EX[f"Team_{make_uri_name(tn)}"] == t_uri)
        assigned_role = random.choice(team_roles[t_name])
        r_uri = role_uris[assigned_role]

        g.add((p_uri, RDF.type, EX.Person))
        g.add((p_uri, RDFS.label, Literal(name)))
        g.add((p_uri, RDFS.comment, Literal(f"Employee {name} working as {assigned_role} on the {t_name} team.")))
        g.add((p_uri, EX.memberOf, t_uri))
        g.add((p_uri, EX.hasRole, r_uri))

    # Team Managers
    for t_uri, members in team_members_map.items():
        if members:
            g.add((t_uri, EX.managedBy, members[0]))

    # Processes & Approval Steps with Spend Limits
    processes_data = [
        {
            "name": "Hardware Procurement Process",
            "steps": [
                ("Manager Endorsement", "IT Support Specialist", 500.00),
                ("Finance Spend Sign-off", "Procurement Specialist", 2500.00)
            ]
        },
        {
            "name": "Production System Access Request",
            "steps": [
                ("Security Compliance Check", "Security Engineer", 0.00),
                ("Lead System Approval", "DevOps Engineer", 0.00)
            ]
        },
        {
            "name": "SaaS Procurement Workflow",
            "steps": [
                ("Department Head Review", "HR Partner", 1000.00),
                ("Vendor Security Assessment", "AppSec Specialist", 5000.00),
                ("Executive Spend Clearance", "Financial Accountant", 25000.00)
            ]
        },
        {
            "name": "High Value Infrastructure Upgrade",
            "steps": [
                ("Architectural Review", "Cloud Architect", 10000.00),
                ("CFO Approval Step", "Vendor Manager", 100000.00)
            ]
        },
        {
            "name": "Standard Software Request",
            "steps": [
                ("Helpdesk Auto Verification", "System Administrator", 250.00)
            ]
        }
    ]

    for proc in processes_data:
        p_name = proc["name"]
        p_uri = EX[f"Proc_{make_uri_name(p_name)}"]
        
        g.add((p_uri, RDF.type, EX.Process))
        g.add((p_uri, RDFS.label, Literal(p_name)))
        g.add((p_uri, RDFS.comment, Literal(f"Administrative governance workflow: {p_name}.")))

        for step_label, approver_role, limit in proc["steps"]:
            s_uri = EX[f"Step_{make_uri_name(p_name)}_{make_uri_name(step_label)}"]
            r_uri = role_uris[approver_role]

            g.add((s_uri, RDF.type, EX.ApprovalStep))
            g.add((s_uri, RDFS.label, Literal(step_label)))
            g.add((s_uri, RDFS.comment, Literal(f"Approval stage '{step_label}' assigned to {approver_role} with spend limit ${limit:.2f}.")))
            g.add((s_uri, EX.approvedBy, r_uri))
            g.add((s_uri, EX.spendLimit, Literal(limit, datatype=XSD.decimal)))

            g.add((p_uri, EX.hasStep, s_uri))

    return g

if __name__ == "__main__":

    path = "onboarding-data.ttl"

    graph = build_annotated_onboarding_graph()
    
    # Serialize complete graph with ontology schema and instances
    turtle_output = graph.serialize(format="turtle")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(turtle_output)
        
    print(f"Written to {path}")

