import MapKit
import SwiftUI

var issues: [Issue] = [
    .init(title: "Illegal Dumping", coordinate: .init(latitude: 41.3935, longitude: 2.1624), status: .active, category: .garbage),
    .init(title: "Recycling Not Collected", coordinate: .init(latitude: 41.3933, longitude: 2.1648), status: .active, category: .garbage),
    .init(title: "Other Concerns", coordinate: .init(latitude: 41.3902, longitude: 2.1616), status: .active, category: .other),
    .init(title: "No Signal Area", coordinate: .init(latitude: 41.3916, longitude: 2.1705), status: .resolved, category: .cellularConnection),
    .init(title: "Air Pollution", coordinate: .init(latitude: 41.3931, longitude: 2.1647), status: .resolved, category: .air),
    .init(title: "Dog Poop", coordinate: .init(latitude: 41.3891, longitude: 2.1671), status: .active, category: .pets),
    .init(title: "Metro Delay", coordinate: .init(latitude: 41.3918, longitude: 2.1652), status: .resolved, category: .metro),
    .init(title: "Sidewalk Repair Needed", coordinate: .init(latitude: 41.3872, longitude: 2.1690), status: .active, category: .infrastructure),
    .init(title: "Public Space Occupied", coordinate: .init(latitude: 41.3920, longitude: 2.1675), status: .resolved, category: .publicSpaces),
    .init(title: "Broken Streetlights", coordinate: .init(latitude: 41.3885, longitude: 2.1600), status: .active, category: .infrastructure),
    .init(title: "Unsafe Biking Path", coordinate: .init(latitude: 41.3897, longitude: 2.1633), status: .resolved, category: .bicycles),
    .init(title: "Water Main Break", coordinate: .init(latitude: 41.3879, longitude: 2.1682), status: .active, category: .water),
    .init(title: "Traffic Noise", coordinate: .init(latitude: 41.3883, longitude: 2.1698), status: .resolved, category: .noise),
    .init(title: "Shop Closed Down", coordinate: .init(latitude: 41.3905, longitude: 2.1664), status: .active, category: .commerce),
    .init(title: "Illegal Street Vendors", coordinate: .init(latitude: 41.3922, longitude: 2.1627), status: .resolved, category: .commerce),
    .init(title: "Stray Animals", coordinate: .init(latitude: 41.3869, longitude: 2.1659), status: .active, category: .pets),
    .init(title: "Parking Meter Broken", coordinate: .init(latitude: 41.3876, longitude: 2.1641), status: .resolved, category: .parking),
    .init(title: "Overflowing Trash Bins", coordinate: .init(latitude: 41.3910, longitude: 2.1703), status: .active, category: .garbage),
    .init(title: "Broken Bike Share", coordinate: .init(latitude: 41.3899, longitude: 2.1696), status: .resolved, category: .bicycles),
    .init(title: "Loud Parties", coordinate: .init(latitude: 41.3939, longitude: 2.1605), status: .active, category: .noise),
    .init(title: "Housing Rent Increase", coordinate: .init(latitude: 41.3927, longitude: 2.1614), status: .resolved, category: .rentHousing),
    .init(title: "Bus Route Cancellation", coordinate: .init(latitude: 41.3912, longitude: 2.1629), status: .active, category: .bus),
    .init(title: "Industrial Emissions", coordinate: .init(latitude: 41.3924, longitude: 2.1684), status: .resolved, category: .air),
    .init(title: "Lost Pet", coordinate: .init(latitude: 41.3887, longitude: 2.1673), status: .active, category: .pets),
    .init(title: "Illegal Parking", coordinate: .init(latitude: 41.3937, longitude: 2.1692), status: .resolved, category: .parking),
    .init(title: "Contaminated Water", coordinate: .init(latitude: 41.3903, longitude: 2.1618), status: .active, category: .water),
    .init(title: "Need More Benches", coordinate: .init(latitude: 41.3894, longitude: 2.1645), status: .resolved, category: .publicSpaces),
    .init(title: "4G Network Down", coordinate: .init(latitude: 41.3915, longitude: 2.1632), status: .active, category: .cellularConnection),
    .init(title: "Vandalism", coordinate: .init(latitude: 41.3926, longitude: 2.1667), status: .resolved, category: .security),
    .init(title: "Soil Contamination", coordinate: .init(latitude: 41.3907, longitude: 2.1658), status: .active, category: .soil)
]

final class CurrentCoordinateHolder {
    var current: CLLocationCoordinate2D = .init(latitude: 41.3922, longitude: 2.1627)
}

struct MapView: View {
    
    @State private var reports = issues
    
    @State private var isReportScreenOpen = false
    
    @State private var position = MapCameraPosition.region(
        .init(
            center: .init(latitude: 41.3922, longitude: 2.1627),
            span: .init(latitudeDelta: -10, longitudeDelta: -10)
        )
    )
    
    private var currentLocationHolder = CurrentCoordinateHolder()
    
    var body: some View {
        MapReader { proxy in
            ZStack {
                Map(position: $position) {
                    ForEach(reports) { issue in
                        Marker(
                            issue.title,
                            systemImage: issue.category.icon,
                            coordinate: issue.coordinate
                        ).tint(issue.status.color)
                    }
                }
                .mapControlVisibility(.hidden)
                .mapStyle(.standard)
                .onMapCameraChange(frequency: .continuous) { context in
                    currentLocationHolder.current = context.region.center
                }
                VStack {
                    HStack {
                        Spacer()
                        Button(action: {}) {
                            Image(systemName: "person.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 20)
                        }
                        .buttonBorderShape(.circle)
                        .buttonStyle(.bordered)
                        .background(.regularMaterial)
                        .clipShape(Circle())
                        .compositingGroup()
                    }.padding()
                    Spacer()
                    Button(action: { isReportScreenOpen.toggle() }) {
                        Label(
                            title: { Text("Report Location") },
                            icon: { Image(systemName: "exclamationmark.bubble.fill") }
                        )
                    }
                    .buttonStyle(.borderedProminent)
                    .buttonBorderShape(.capsule)
                    .font(.title)
                    .padding(.bottom, 30)
                }.padding()
                Image(systemName: "mappin")
                    .font(.largeTitle)
                    .foregroundStyle(.tint)
            }
            .sheet(isPresented: $isReportScreenOpen) {
                IssueReportForm(
                    reports: $reports,
                    coordinate: currentLocationHolder.current
                )
            }
        }.tint(.purple)
    }
}

#Preview {
    MapView()
}

struct Issue: Identifiable {
    let id = UUID()
    var title: String
    var description: String?
    var image: UIImage?
    var coordinate: CLLocationCoordinate2D
    var status: Status
    var category: Category
    
    init(title: String, description: String? = nil, image: UIImage? = nil, coordinate: CLLocationCoordinate2D, status: Status, category: Category) {
        self.title = title
        self.description = description
        self.image = image
        self.coordinate = coordinate
        self.status = status
        self.category = category
    }
    
    enum Status {
        case pending
        case active
        case resolved
        
        var color: Color {
            switch self {
            case .pending: return .yellow
            case .active: return .orange
            case .resolved: return .green
            }
        }
    }
}

enum Category: String, CaseIterable {
    case bus = "Bus"
    case metro = "Metro"
    case bicycles = "Bicycles"
    case rentHousing = "Rent Housing"
    case pets = "Pets"
    case parking = "Parking"
    case garbage = "Garbage"
    case trees = "Trees"
    case publicSpaces = "Public Spaces"
    case commerce = "Commerce"
    case infrastructure = "Infrastructure"
    case cellularConnection = "Cellular Connection"
    case air = "Air"
    case water = "Water"
    case noise = "Noise"
    case soil = "Soil"
    case security = "Security"
    case other = "Other"
    
    var icon: String {
        switch self {
        case .bus: return "bus"
        case .metro: return "tram.fill"
        case .bicycles: return "bicycle"
        case .rentHousing: return "house.fill"
        case .pets: return "pawprint.fill"
        case .parking: return "car.fill"
        case .garbage: return "trash.fill"
        case .trees: return "tree.fill"
        case .publicSpaces: return "building.2"
        case .commerce: return "cart.fill"
        case .infrastructure: return "wrench.and.screwdriver.fill"
        case .cellularConnection: return "antenna.radiowaves.left.and.right"
        case .air: return "wind"
        case .water: return "drop.fill"
        case .noise: return "speaker.3.fill"
        case .soil: return "leaf.arrow.circlepath"
        case .security: return "lock.fill"
        case .other: return "questionmark.circle.fill"
        }
    }
}


