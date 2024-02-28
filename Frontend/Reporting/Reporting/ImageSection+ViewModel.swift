import SwiftUI
import PhotosUI
import CoreTransferable

extension ImageSection {
    
    @Observable final class ViewModel {
        
        private(set) var imageState: ImageState = .empty
        
        var imageSelection: PhotosPickerItem? = nil
        
        func set(imageSelection: PhotosPickerItem?) {
            self.imageSelection = imageSelection
            if let imageSelection {
                let progress = loadTransferable(from: imageSelection)
                imageState = .loading(progress)
            } else {
                imageState = .empty
            }
        }
        
        private func loadTransferable(from imageSelection: PhotosPickerItem) -> Progress {
            return imageSelection.loadTransferable(type: ProfileImage.self) { result in
                DispatchQueue.main.async {
                    guard imageSelection == self.imageSelection else {
                        print("Failed to get the selected item.")
                        return
                    }
                    switch result {
                    case .success(let profileImage?):
                        self.imageState = .success(profileImage.image)
                    case .success(nil):
                        self.imageState = .empty
                    case .failure(let error):
                        self.imageState = .failure(error)
                    }
                }
            }
        }
        
        enum ImageState {
            case empty
            case loading(Progress)
            case success(Image)
            case failure(Error)
        }
        
        enum TransferError: Error {
            case importFailed
        }
        
        struct ProfileImage: Transferable {
            let image: Image
            
            static var transferRepresentation: some TransferRepresentation {
                DataRepresentation(importedContentType: .image) { data in
                    guard let uiImage = UIImage(data: data) else {
                        throw TransferError.importFailed
                    }
                    let image = Image(uiImage: uiImage)
                    return ProfileImage(image: image)
                }
            }
        }
    }
}
