import SwiftUI
import PhotosUI
import Observation

struct ImageSection: View {
    
    @Bindable var viewModel: ViewModel
    
    var body: some View {
        switch viewModel.imageState {
        case let .success(image):
            Section {
                HStack {
                    Spacer()
                    image
                        .resizable()
                        .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
                        .scaledToFill()
                        .aspectRatio(contentMode: .fit)
                        .frame(maxHeight: 250)
                    Spacer()
                }
                .padding(.vertical)
                PhotosPicker(selection: $viewModel.imageSelection,
                             matching: .images,
                             photoLibrary: .shared()) {
                    Label("Add Photo", systemImage: "camera.fill")
                }
            }
        case .loading:
            HStack {
                Spacer()
                ProgressView()
                Spacer()
            }
        default:
            PhotosPicker(selection: $viewModel.imageSelection,
                         matching: .images,
                         photoLibrary: .shared()) {
                Label("Add Photo", systemImage: "camera.fill")
            }
        }
    }
}
