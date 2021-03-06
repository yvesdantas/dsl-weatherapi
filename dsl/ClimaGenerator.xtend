/*
 * generated by Xtext 2.26.0-SNAPSHOT
 */
package org.xtext.example.minhadsl.generator

import org.eclipse.emf.ecore.resource.Resource
import org.eclipse.xtext.generator.AbstractGenerator
import org.eclipse.xtext.generator.IFileSystemAccess2
import org.eclipse.xtext.generator.IGeneratorContext
import org.xtext.example.minhadsl.clima.Clima

/**
 * Generates code from your model files on save.
 * 
 * See https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#code-generation
 */
class ClimaGenerator extends AbstractGenerator {

	override void doGenerate(Resource resource, IFileSystemAccess2 fsa, IGeneratorContext context) {
		fsa.generateFile('dadosClimaticos.json', '[\n{\n' + 
			resource.allContents
				.filter(Clima)
				.map[compilaSaida]
				.join(',\n{\n') + ']')
	}
	
	private def compilaSaida(Clima c) '''
		"Cidade": "«c.cidade»",
		"Data início": "«c.dataInicio»",
		"Data fim": "«c.dataFim»"
		}
'''
}