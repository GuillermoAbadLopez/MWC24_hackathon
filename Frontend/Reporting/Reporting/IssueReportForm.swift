import MapKit
import SwiftUI

struct IssueReportForm: View {
    
    @Environment(\.dismiss) var dismiss
    
    @Binding var reports: [Issue]
    let coordinate: CLLocationCoordinate2D
    @State private var title = String()
    @State private var description = String()
    @State private var selectedCategory: Category = .bus
    
    @State private var imageSectionViewModel = ImageSection.ViewModel()
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    TextField("Title", text: $title)
                    Picker("Category", selection: $selectedCategory) {
                        ForEach(Category.allCases, id: \.self) { category in
                            HStack {
                                Text(category.rawValue)
                                Spacer()
                                Image(systemName: category.icon)
                            }.tag(category)
                        }
                    }
                }
                
                ImageSection(viewModel: imageSectionViewModel)
                
                Section(header: Text("Description")) {
                    TextEditor(text: $description)
                        .lineLimit(30, reservesSpace: true)
                        .frame(minHeight: 250)
                }
            }.toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: addReport) {
                        Text("Done").bold()
                    }
                }
            }
            .navigationTitle("Add Report")
            .navigationBarTitleDisplayMode(.inline)
        }.tint(.purple)
    }
    
    private func addReport() {
        reports.append(
            .init(
                title: title,
                coordinate: coordinate,
                status: .pending,
                category: selectedCategory
            )
        )
        dismiss()
    }
    
}

#Preview {
    IssueReportForm(reports: .constant([]), coordinate: .init())
}
